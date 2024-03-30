import psutil

def display_users():
    users = psutil.users()
    print("User Information:")
    for user in users:
        print(f"Username: {user.name}, Terminal: {user.terminal}, Host: {user.host}, Started: {user.started}")
    print()