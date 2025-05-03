import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} for open ports...")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")

if __name__ == "__main__":
    target_host = input("Enter target host (IP or domain): ")
    scan_ports(target_host, 1, 1000)
