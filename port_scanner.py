
import socket

def scan_port(host, port):
    """Check if a port is open on a given host."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def main():
    target = "scanme.nmap.org"  
    print(f"Scanning {target}...")
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 
                    993, 995, 1723, 3306, 3389, 5900, 8080]
    
    for port in common_ports:
        if scan_port(target, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")  

if __name__ == "__main__":
    main()
