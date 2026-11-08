import customtkinter as ctk
import psutil

app = ctk.CTk()
app.title("DesktopPad")
app.geometry("400x300")

cpu_usage = psutil.cpu_percent(interval=0)
ram_usage = psutil.virtual_memory().percent

label = ctk.CTkLabel(
    app,
    text=f"CPU: {cpu_usage}%\nRAM: {ram_usage}%"
)

label.pack(pady=40)

app.mainloop()