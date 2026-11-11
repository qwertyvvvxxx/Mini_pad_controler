import pytest

from desktop_app.monitoring.system_monitor import SystemMonitor

@pytest.fixture
def system_data():
    monitor = SystemMonitor()
    return monitor.get_data()


def test_get_data(system_data):
    assert isinstance(system_data, dict)

def test_cpu_metrics(system_data):
    assert "cpu" in system_data
    assert isinstance(system_data["cpu"], (int, float))
    assert 0 <= system_data["cpu"] <= 100

def test_ram_metrics(system_data):
    assert "ram_percent" in system_data
    assert "ram_total_gb" in system_data
    assert isinstance(system_data["ram_percent"], (int, float))
    assert system_data["ram_total_gb"] > 0

