import pytest
from actuator_processor import Actuator


def test_initial_state():
    a = Actuator("bp-01")
    result = a.summary()
    assert result["actuator_id"] == "bp-01"
    assert result["final_state"] == "IDLE"
    assert result["rejected_commands"] == 0
    assert result["time_in_state"] == {"IDLE": 0, "CHARGING": 0, "DISCHARGING": 0}


def test_valid_transition_returns_true():
    a = Actuator("bp-01")
    assert a.apply_command("SET_CHARGING", 0) is True


def test_invalid_transition_returns_false():
    a = Actuator("bp-01")
    a.apply_command("SET_CHARGING", 0)
    assert a.apply_command("SET_DISCHARGING", 10) is False  # CHARGING → DISCHARGING invalid


def test_state_does_not_change_on_rejection():
    a = Actuator("bp-01")
    a.apply_command("SET_CHARGING", 0)
    a.apply_command("SET_DISCHARGING", 10)  # rejected
    assert a.summary()["final_state"] == "CHARGING"


def test_time_in_state():
    a = Actuator("bp-01")
    a.apply_command("SET_CHARGING", 0)     # → CHARGING
    a.apply_command("SET_IDLE", 60)        # CHARGING for 60s → IDLE
    a.apply_command("SET_DISCHARGING", 90) # IDLE for 30s → DISCHARGING
    a.apply_command("SET_IDLE", 120)       # DISCHARGING for 30s → IDLE
    times = a.summary()["time_in_state"]
    assert times["CHARGING"] == 60
    assert times["IDLE"] == 30
    assert times["DISCHARGING"] == 30


def test_multiple_rejections_counted():
    a = Actuator("bp-01")
    a.apply_command("SET_CHARGING", 0)
    a.apply_command("SET_DISCHARGING", 5)   # rejected
    a.apply_command("SET_DISCHARGING", 10)  # rejected
    a.apply_command("SET_IDLE", 15)
    assert a.summary()["rejected_commands"] == 2
