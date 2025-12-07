import subprocess

def check_ping(ip):
    command = ["ping", "-n", "1", ip]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def scan_network(network_prefix):
    active_ips = []
    for num in range(1, 20):
        ip = f"{network_prefix}.{num}"
        print("Pinging", ip)
        if check_ping(ip):
            active_ips.append(ip)
    return active_ips

network_prefix = "192.168.1"
active_hosts = scan_network(network_prefix)
print(active_hosts)