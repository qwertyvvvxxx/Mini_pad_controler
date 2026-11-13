import pytest

from desktop_app.device.device_simulator import DeviceSimulator, Screen


@pytest.fixture
def device():
    device = DeviceSimulator()
    return device

def test_go_home(device):
    assert device.go_home() == "HOME"

def test_switch_screen(device):
    assert device.switch_screen(Screen.MENU) == "MENU"
    assert device.switch_screen(Screen.SYSTEM) == "SYSTEM"
    assert device.switch_screen(Screen.APPS) == "APPS"


