import subprocess

def display_ssh_connections():
    try:
        ssh_output = subprocess.check_output(["netstat", "-tnp"]).decode("utf-8")
        print("Active SSH Connections:")
        for line in ssh_output.split('\n'):
            if "ESTABLISHED" in line and "ssh" in line:
                parts = line.split()
                remote_address = parts[3].split(':')[0]
                print(f"Remote Address: {remote_address}")
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve SSH connections.")