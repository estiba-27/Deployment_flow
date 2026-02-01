from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Deployment
from state_machine import DeploymentStateMachine

app = FastAPI(title="Deployment Approval Workflow")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DeploymentCreate(BaseModel):
    name: str

@app.post("/deployments")
def create_deployment(data: DeploymentCreate, db: Session = Depends(get_db)):
    sm = DeploymentStateMachine()
    deployment = Deployment(name=data.name, state=sm.state)
    db.add(deployment)
    db.commit()
    db.refresh(deployment)
    return {"id": deployment.id, "name": deployment.name, "state": deployment.state}

@app.post("/deployments/{deployment_id}/approve")
def approve_deployment(deployment_id: int, db: Session = Depends(get_db)):
    deployment = db.query(Deployment).filter_by(id=deployment_id).first()
    if not deployment:
        raise HTTPException(status_code=404, detail="Deployment not found")

    sm = DeploymentStateMachine(initial_state=deployment.state)
    try:
        sm.approve()
    except Exception:
        raise HTTPException(status_code=400, detail=f"Cannot approve from {deployment.state}")

    deployment.state = sm.state
    db.commit()
    return {"id": deployment.id, "state": deployment.state}

@app.post("/deployments/{deployment_id}/reject")
def reject_deployment(deployment_id: int, db: Session = Depends(get_db)):
    deployment = db.query(Deployment).filter_by(id=deployment_id).first()
    if not deployment:
        raise HTTPException(status_code=404, detail="Deployment not found")

    sm = DeploymentStateMachine(initial_state=deployment.state)
    sm.reject()
    deployment.state = sm.state
    db.commit()
    return {"id": deployment.id, "state": deployment.state}

@app.get("/deployments")
def list_deployments(db: Session = Depends(get_db)):
    deployments = db.query(Deployment).all()
    return [{"id": d.id, "name": d.name, "state": d.state} for d in deployments]

