## Python Codes Projects

A collection of small-to-mid Python projects and experiments, grouped by topic:

- `blackbox codes`: Assorted scripts for networking, hashing, and request syntax exploration.
- `python-network-projects`: Simple client/server demos and network exercises.
- `python-playground`: Practice problems and exercises (data structures, small utilities).
- `python-security-projects`: Educational security tooling (keylogger, brute force demos, RAT components, network attacks, MITM, simple antivirus heuristics).

This repository is intended for learning and experimentation.

### Prerequisites
- Python 3.9+ (3.10+ recommended)
- Any terminal: PowerShell, Command Prompt, Git Bash/WSL (Windows) or Bash/Zsh (macOS/Linux)

### Getting Started
1. Clone or open the project directory: `D:\Python-codes-projects`
2. (Recommended) Create and activate a virtual environment:
   - Create: `python -m venv .venv`
   - Activate (PowerShell): `./.venv/Scripts/Activate.ps1`
   - Activate (Cmd): `\.venv\Scripts\activate.bat`
   - Activate (Bash: Git Bash/WSL/macOS/Linux): `source .venv/bin/activate`
3. Install any per-project requirements if present. Most scripts here are standalone and use the standard library; consult subproject READMEs if available.

### Repository Structure

- `blackbox codes/`
  - `blackbox1/`: Base64, HTTP request, and SHA1 helpers
  - `blackbox2/`: TCP client and phone-number brute force example
  - `blackbox6/`: MD5 hashing and TCP socket example
  - `blackbox7/`: Simple checksum brute force and a lightweight data store
  - `SYNTAX/`: Small syntax/reference snippets (HTTP/TCP/UDP examples, subprocess usage)

- `python-network-projects/`
  - `Server_Client Project/`: Minimal TCP server and client with a sample payload

- `python-playground/`
  - `data_structures/`: Hashing and dictionary/list practice
  - `exercises/`: Assorted coding exercises (calculator, class tasks, password checker, binary representation, sys utilities)

- `python-security-projects/`
  - `src/antivirus/`: Very basic antivirus heuristics
  - `src/brute_force/`: Demonstration brute-force logic (passwords/pins)
  - `src/keylogger/`: Keyboard logging example (logs to file)
  - `src/network_attacks/`: SYN flooding example
  - `src/MITM Attack Project/`: ARP spoofing demos
  - `src/RAT project/`: Keyboard/Mouse/Screen client-server samples

### How to Run

Most scripts can be executed directly with Python. Examples below assume you have activated your virtual environment in the repository root.

- Run a simple script:
  - Any terminal: `python "python-playground/exercises/PasswordChecker.py"`

- Run the basic client/server demo:
  - Start server: `python "python-network-projects/Server_Client Project/Server.py"`
  - In a new terminal, start client: `python "python-network-projects/Server_Client Project/Client.py"`

- Run the keylogger (educational example):
  - `python "python-security-projects/src/keylogger/Keylogger.py"`
  - Output file: `python-security-projects/src/keylogger/keyboard_log.txt`

- Run SYN flooding demo (requires administrative privileges and may need platform-specific networking permissions):
  - `python "python-security-projects/src/network_attacks/SYN_Flooding.py"`

- Run ARP spoofing demo (requires admin/root and appropriate network environment):
  - `python "python-security-projects/src/MITM Attack Project/arp_spoof_computer.py"`
  - `python "python-security-projects/src/MITM Attack Project/arp_spoof_router.py"`

Refer to the subproject READMEs for any additional notes:
- `python-security-projects/README.md`
- `python-network-projects/README.md`
- `python-playground/README.md`
- `blackbox codes/README.md` (if present)

### Notes on Dependencies

This repository does not currently include a unified `requirements.txt`. Most scripts use only the Python standard library. If a script requires a third-party package, install it ad-hoc, for example:

```bash
pip install requests pynput scapy
```

Only install what you need for the specific script you are running.

### Security and Ethics

Some code in `python-security-projects` demonstrates offensive techniques for educational purposes only:

- Use only in controlled lab environments or where you have explicit authorization.
- Do not use against systems, networks, or data you do not own or have permission to test.
- You are responsible for complying with all applicable laws and policies.

### Troubleshooting

- If a script requires admin privileges, run your terminal as Administrator (Windows) or use `sudo` (macOS/Linux).
- On antivirus false-positives, either whitelist the folder locally or run in an isolated VM.
- For networking demos, ensure your firewall allows local traffic and that the chosen ports are open.
- If an import fails, verify the working directory and `PYTHONPATH`, or run the script using its full path from the repository root as shown above.

### Contributing

This is a personal learning repository. If you spot issues, feel free to open an issue or propose an improvement via a pull request.


