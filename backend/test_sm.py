from state_machine import DeploymentStateMachine

dsm = DeploymentStateMachine()

print("Initial:", dsm.state)

dsm.approve_manager()
print("After manager approval:", dsm.state)

dsm.approve_devops()
print("After devops approval:", dsm.state)

# This should FAIL if uncommented
# dsm.reject()

