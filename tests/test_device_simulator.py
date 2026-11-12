import pytest

from desktop_app.device_simulator import DeviceSimulator, Screen


@pytest.fixture
def device():
    device = DeviceSimulator()
    return device

def test_go_home(device):
    assert device.go_home() == "Current screen: HOME"

def test_switch_screen(device):
    assert device.switch_screen(Screen.MENU) == "Current screen: MENU"
    assert device.switch_screen(Screen.SYSTEM) == "Current screen: SYSTEM"
    assert device.switch_screen(Screen.APPS) == "Current screen: APPS"


