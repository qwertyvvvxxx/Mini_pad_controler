import psutil

class SystemMonitor():
    def get_data(self):
        cpu_usage = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory()

        return {
            "cpu": cpu_usage,
            "ram_percent": ram.percent,
            "ram_total_gb": round(ram.total / 1024**3, 1)
        }

