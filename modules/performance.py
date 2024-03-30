import psutil

def display_performance_metrics():
    print("System Performance Metrics:")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print()