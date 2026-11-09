import customtkinter as ctk
from monitoring.system_monitor import SystemMonitor

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Mini_Pad_V1")
app.geometry("520x200")

monitor = SystemMonitor()

system_data = monitor.get_data()

cpu_frame = ctk.CTkFrame(app)
ram_frame = ctk.CTkFrame(app)

ram_frame.grid(row=0, column=0,padx=20, pady=10)
cpu_frame.grid(row=0, column=1,padx=20, pady=10)

cpu_label = ctk.CTkLabel(
    cpu_frame,
    text=f"CPU: {system_data["cpu"]}%\n"
)

ram_label = ctk.CTkLabel(
    ram_frame,
    text=f"RAM: {system_data["ram_percent"]}%\n"
         f"RAM: {system_data["ram_total_gb"]} GB"
)

ram_label.pack(pady=30, padx=5)
cpu_label.pack(pady=30)


ram_progress_bar = ctk.CTkProgressBar(ram_frame)
cpu_progres_bar = ctk.CTkProgressBar(cpu_frame)

ram_progress_bar.pack(padx=10, pady=5)
cpu_progres_bar.pack(padx=10, pady=5)

def update_metrics():
    data_to_update = monitor.get_data()

    cpu_label.configure(

        text=f"CPU: {data_to_update["cpu"]}%\n"
    )

    cpu_progres_bar.set(data_to_update["cpu"] / 100)

    ram_label.configure(

        text=f"RAM: {data_to_update["ram_percent"]}%\n"
             f"RAM: {data_to_update["ram_total_gb"]} GB"
    )

    ram_progress_bar.set(data_to_update["ram_percent"] / 100)

    app.after(1000, update_metrics)

update_metrics()

app.mainloop()