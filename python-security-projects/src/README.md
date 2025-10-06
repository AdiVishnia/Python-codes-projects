# src

Module overview and basic run notes (for learning use only):

## antivirus
- `AntiVirus.py`: Simple local scan/hashing demo. Adjust scan paths and permissions per OS.

## brute_force
- `BruteForce.py`: Research examples of brute forcing inputs/hashes. Run only on your own data with permission.

## keylogger
- `Keylogger.py`: Keylogger writing to `keyboard_log.txt`. As long as the keylogger terminal is running, it will detect keystrokes. Requires elevated privileges. Use privately and responsibly.

## network_attacks
- `SYN_Flooding.py`: SYN flood demonstration in LAN. Note: This basic example often doesn't do much as the default gateway's firewall typically blocks it. Requires elevated privileges and proper network interface.

## MITM Attack Project
Demonstrates a Man‑in‑the‑Middle attack using ARP spoofing in LAN.
- `arp_spoof_computer.py`: Targets the victim computer.
- `arp_spoof_router.py`: Targets the router/default gateway.
- `Attacked computer ARP table change.jpg`: Screenshot of the victim's ARP table after spoofing.

Usage notes:
- Education and lab use only, on systems you own or have explicit permission to test.
- May require Administrator/Root privileges and the correct network interface.
- Before running, update IP addresses and interface names in the code to match your topology.

## RAT project
Demonstration tools for remote control in a controlled lab:
- Keyboard: `keyboard_server.py`, `keyboard_client.py`
- Mouse: `mouse_server.py`, `mouse_client.py`
- Screen: `screen_server.py`, `screen_client.py`

General notes (for learning purposes only):
- Set correct IP/port in code before running.
- Start server before client; verify the network interface.
- Some tools require Administrator/Root privileges.
- Use only on systems you own or with explicit authorization.