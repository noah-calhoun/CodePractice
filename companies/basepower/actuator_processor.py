"""
Base Power Technical Screen
----------------------------
Model a home battery actuator as a class.

The actuator has three states: IDLE, CHARGING, DISCHARGING
It always starts in IDLE.

Valid transitions:
    IDLE        → CHARGING      ("SET_CHARGING")
    IDLE        → DISCHARGING   ("SET_DISCHARGING")
    CHARGING    → IDLE          ("SET_IDLE")
    DISCHARGING → IDLE          ("SET_IDLE")

Implement the Actuator class below.
"""

VALID_TRANSITIONS: dict[str, dict[str, str]] = {
    "IDLE":        {"SET_CHARGING": "CHARGING", "SET_DISCHARGING": "DISCHARGING"},
    "CHARGING":    {"SET_IDLE": "IDLE"},
    "DISCHARGING": {"SET_IDLE": "IDLE"},
}


class Actuator:
    def __init__(self, actuator_id: str):
        """Initialize the actuator in IDLE state."""
        self.state = 'IDLE'
        self.id = actuator_id
        self.rejected = 0
        self.stateTime = {
            "IDLE": 0,
            "CHARGING": 0,    
            "DISCHARGING": 0, 
        }
        self.previousTimestamp = 0
    
    def setStateTime(self, state, timestamp):
        self.stateTime[state] = self.stateTime.get(state, 0) + (timestamp - self.previousTimestamp)
        self.previousTimestamp = timestamp
        return

    def apply_command(self, command: str, timestamp: int) -> bool:
        """
        Attempt to transition state via command at the given timestamp.

        Returns True if the transition was valid and applied.
        Returns False if the transition was invalid (state does not change).

        Timestamps are always strictly increasing.
        Time is accumulated between valid transitions only.
        The open-ended duration after the last command is not counted.
        """
        validTransition = VALID_TRANSITIONS.get(self.state)
        if command in validTransition:
            self.stateTime[self.state] += timestamp - self.previousTimestamp
            self.previousTimestamp = timestamp
            self.state = VALID_TRANSITIONS[self.state][command]
            return True
        else: 
            self.rejected += 1
            return False
        

    def summary(self) -> dict:
        """
        Return a summary dict:
        {
            "actuator_id":       str,
            "final_state":       str,
            "rejected_commands": int,
            "time_in_state":     dict[str, int]  # seconds per state
        }
        """
        return {
            "actuator_id": self.id,
            "final_state": self.state,
            "rejected_commands": self.rejected,
            "time_in_state": self.stateTime
        }
        
