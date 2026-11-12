import customtkinter as ctk

from desktop_app.device_simulator import DeviceSimulator
from desktop_app.interface.dashboard import Dashboard
from desktop_app.monitoring.system_monitor import SystemMonitor
from config import APPEARANCE_MODE, COLOR_THEME

ctk.set_appearance_mode(APPEARANCE_MODE)
ctk.set_default_color_theme(COLOR_THEME)

app = ctk.CTk()

monitor = SystemMonitor()
device_simulator = DeviceSimulator()

dashboard = Dashboard(app, monitor, device_simulator)

app.mainloop()