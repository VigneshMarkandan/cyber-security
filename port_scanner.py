import socket
import argparse

def scan_ports(target_ip, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set a timeout for the connection
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def main():
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('target', type=str, help='The target IP address')
    parser.add_argument('--ports', type=str, default='1-1024',
                        help='The range of ports to scan (e.g., 1-1024)')
    
    args = parser.parse_args()
    
    target_ip = args.target
    port_range = args.ports.split('-')
    start_port = int(port_range[0])
    end_port = int(port_range[1])
    
    print(f"Scanning ports from {start_port} to {end_port} on {target_ip}...")
    ports_to_scan = range(start_port, end_port + 1)
    open_ports = scan_ports(target_ip, ports_to_scan)
    
    if open_ports:
        print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_ip}.")

if __name__ == '__main__':
    main()
