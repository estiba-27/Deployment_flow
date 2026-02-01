from transitions import Machine

class DeploymentStateMachine:
    states = [
        "requested",
        "approved_by_QA",
        "approved_by_devops",
        "executed",
        "rejected",
    ]

    def __init__(self, initial_state="requested"):
        self.state = initial_state
        self.machine = Machine(
            model=self,
            states=DeploymentStateMachine.states,
            initial=initial_state,
        )
        self.machine.add_transition("approve", "requested", "approved_by_QA")
        self.machine.add_transition("approve", "approved_by_QA", "approved_by_devops")
        self.machine.add_transition("approve", "approved_by_devops", "executed")
        self.machine.add_transition("reject", "*", "rejected")

