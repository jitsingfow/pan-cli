import psutil

def display_disk_usage():
    partitions = psutil.disk_partitions()
    print("Disk Usage:")
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Partition: {partition.device}")
        print(f"  Total: {usage.total / (1024 * 1024 * 1024):.2f} GB")
        print(f"  Used: {usage.used / (1024 * 1024 * 1024):.2f} GB")
        print(f"  Free: {usage.free / (1024 * 1024 * 1024):.2f} GB")
        print(f"  Percentage Used: {usage.percent}%")
        print()