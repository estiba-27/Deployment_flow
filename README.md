# Deployment Approval Workflow System

A backend-driven deployment approval system that enforces **multi-step approvals using a formal state machine**.  
The system exposes REST APIs and a lightweight frontend to manage and visualize deployment lifecycle transitions.

---

## Features

- Create deployment requests
- Enforce multi-stage approvals (Manager → DevOps)
- Reject deployments at any stage
- Deterministic state transitions using a **state machine**
- REST API with FastAPI
- Simple frontend (HTML, CSS, JavaScript)
- Persistent storage with SQLite

---

## Technology Stack

| Layer      | Technology |
|-----------|------------|
| Backend   | Python, FastAPI |
| State Mgmt | `transitions` (state machine library) |
| Database  | SQLite + SQLAlchemy |
| Frontend  | HTML, CSS, Vanilla JavaScript |
| API Docs  | Swagger (FastAPI `/docs`) |

---
## Setup Instructions

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/estiba-27
cd deployment_workflow

2.Backend Setup
Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

Install backend dependencies
pip install -r requirements.txt

3. Initialize the Database
Run the database creation script:

4.Start the Backend Server
cd backend
uvicorn main:app --reload
Backend will be available at:
API Base URL: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs
5.Frontend Setup
cd frontend
python3 -m http.server 8080
Open a new terminal and run:
cd frontend
python3 -m http.server 8080
Open your browser at:
http://localhost:8080
8. API Testing
You can test APIs directly via Swagger:
http://127.0.0.1:8000/docs
Available endpoints:

POST /deployments

POST /deployments/{id}/approve

POST /deployments/{id}/reject

GET /deployments

## Docker Setup 
This project supports running the backend using Docker for consistent and reproducible environments.
Prerequisites

Docker
Docker Compose
Build and run containers
docker compose up --build
Access services

Backend API: http://localhost:8000

Swagger Docs: http://localhost:8000/docs
Stop containers
docker compose down

