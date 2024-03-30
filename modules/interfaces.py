import psutil

def display_network_interfaces():
    interfaces = psutil.net_if_addrs()
    print("Network Interface Information:")
    for interface_name, interface_addresses in interfaces.items():
        print(f"Interface: {interface_name}")
        for address in interface_addresses:
            print(f"  {address.family.name}: {address.address}")
        print()
