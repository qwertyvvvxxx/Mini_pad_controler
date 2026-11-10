from typing import Self

import customtkinter as ctk

from config import UPDATE_INTERVAL, WINDOW_TITLE, WINDOW_GEOMETRY


class Dashboard:
    def __init__(self, app, monitor):
        self.app = app
        self.monitor = monitor

        self.app.title(WINDOW_TITLE)
        self.app.geometry(WINDOW_GEOMETRY)

        system_data = monitor.get_data()

        self.cpu_frame = ctk.CTkFrame(app)
        self.ram_frame = ctk.CTkFrame(app)

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

        def update_metrics():
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

            self.app.after(UPDATE_INTERVAL, update_metrics)

        update_metrics()