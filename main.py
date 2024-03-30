import argparse
from modules import interfaces, disk, processes, users, performance, ssh, version

def main():
    parser = argparse.ArgumentParser(description="PAN - CLI tool for system information and port details")
    parser.add_argument("-i", "--interfaces", action="store_true", help="Display network interface information")
    parser.add_argument("-d", "--disk-usage", action="store_true", help="Display disk usage information")
    parser.add_argument("-p", "--processes", action="store_true", help="Display process management information")
    parser.add_argument("-u", "--users", action="store_true", help="Display user information")
    parser.add_argument("-m", "--metrics", action="store_true", help="Display system performance metrics")
    parser.add_argument("-s", "--ssh", action="store_true", help="Display active SSH connections")
    parser.add_argument("-v", "--version", action="store_true", help="Display version")
    args = parser.parse_args()

    if args.interfaces:
        interfaces.display_network_interfaces()
    elif args.disk_usage:
        disk.display_disk_usage()
    elif args.processes:
        processes.display_processes()
    elif args.users:
        users.display_users()
    elif args.metrics:
        performance.display_performance_metrics()
    elif args.ssh:
        ssh.display_ssh_connections()
    elif args.version:
        version.display_version()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
