import customtkinter as ctk

from config import UPDATE_INTERVAL, WINDOW_TITLE, WINDOW_GEOMETRY
from desktop_app.device_simulator import Screen


class Dashboard:
    def __init__(self, app, monitor,device_simulator):
        self.app = app
        self.monitor = monitor
        self.device = device_simulator

        self.tabview = ctk.CTkTabview(self.app)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_monitor = self.tabview.add("Monitoring")
        self.tab_simulator = self.tabview.add("Device Simulator")


        self.app.title(WINDOW_TITLE)
        self.app.geometry(WINDOW_GEOMETRY)

        system_data = monitor.get_data()

        self.cpu_frame = ctk.CTkFrame(self.tab_monitor)
        self.ram_frame = ctk.CTkFrame(self.tab_monitor)

        self.ram_frame.grid(row=0, column=0,padx=20, pady=10)
        self.cpu_frame.grid(row=0, column=1,padx=20, pady=10)

        self.cpu_label = ctk.CTkLabel(
            self.cpu_frame,
            text=f"CPU: {system_data["cpu"]}%\n"
        )

        self.ram_label = ctk.CTkLabel(
            self.ram_frame,
            text=f"RAM: {system_data["ram_percent"]}%\n"
                 f"RAM: {system_data["ram_total_gb"]} GB"
        )

        self.ram_label.pack(pady=30, padx=5)
        self.cpu_label.pack(pady=30)


        self.ram_progress_bar = ctk.CTkProgressBar(self.ram_frame)
        self.cpu_progres_bar = ctk.CTkProgressBar(self.cpu_frame)

        self.ram_progress_bar.pack(padx=10, pady=5)
        self.cpu_progres_bar.pack(padx=10, pady=5)

        self.update_metrics()
        self.setup_simulator_tab()

    def setup_simulator_tab(self):
        self.screen_label = ctk.CTkLabel(
            self.tab_simulator,
            text=f"Current screen: {self.device.current_screen.value}",
            font=("Arial", 16, "bold")
        )

        self.screen_label.pack(pady=30, padx=5)

        self.btn_menu = ctk.CTkButton(
            self.tab_simulator,
            text="Menu",
            command=lambda: self.on_screen_click(Screen.MENU)
        )

        self.btn_menu.pack(pady=5)

        self.btn_system = ctk.CTkButton(
            self.tab_simulator,
            text="System",
            command=lambda: self.on_screen_click(Screen.SYSTEM)
        )
        self.btn_system.pack(pady=5)

        # 4. Кнопка для переходу в APPS
        self.btn_apps = ctk.CTkButton(
            self.tab_simulator,
            text="Apps",
            command=lambda: self.on_screen_click(Screen.APPS)
        )
        self.btn_apps.pack(pady=5)

        # 5. Кнопка для повернення додому (HOME)
        self.btn_home = ctk.CTkButton(
            self.tab_simulator,
            text="Home",
            command=lambda: self.on_screen_click(Screen.HOME)
        )
        self.btn_home.pack(pady=5)

    def on_screen_click(self, screen):
        self.device.switch_screen(screen)

        self.screen_label.configure(
            text=f"Current screen: {self.device.current_screen.value}"
        )


    def update_metrics(self):
        data_to_update = self.monitor.get_data()

        self.cpu_label.configure(
            text=f"CPU: {data_to_update["cpu"]}%\n"
        )

        self.cpu_progres_bar.set(data_to_update["cpu"] / 100)

        self.ram_label.configure(
            text=f"RAM: {data_to_update["ram_percent"]}%\n"
                 f"RAM: {data_to_update["ram_total_gb"]} GB"
        )

        self.ram_progress_bar.set(data_to_update["ram_percent"] / 100)

        self.app.after(UPDATE_INTERVAL, self.update_metrics)