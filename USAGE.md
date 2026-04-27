# SSH Botnet Usage Guide

A simple, Python-based SSH control unit for executing commands across multiple servers simultaneously.

## Table of Contents
1. [Installation](#installation)
2. [Configuration (Targets File)](#configuration-targets-file)
3. [Running the Tool](#running-the-tool)
4. [Recent Improvements](#recent-improvements)
5. [Security Warning](#security-warning)

---

## Installation

The tool requires Python 3 and the `pexpect` library.

```bash
# Navigate to the directory
cd ~/Desktop/ssh-botnet

# Install dependencies
pip install pexpect
```

## Configuration (Targets File)

Instead of hardcoding credentials, you now provide a file containing your targets. 
Create a text file (e.g., `targets.txt`) with the following format (one line per server):

```text
# host-username-password
192.168.1.10-root-password123
192.168.1.11-admin-pass456
```

## Running the Tool

Execute the script using Python 3:

```bash
python3 ssh_botnet.py
```

1. **File Prompt:** The script will ask: `Chemin du fichier de cibles (format: host-user-password) >> `.
   - Type the name of your file (e.g., `targets.txt`) and press Enter.
2. **Command Prompt:** It will then ask: `Commande à exécuter >> `.
   - Type your command (e.g., `uptime`, `ls`, `whoami`) and press Enter.
3. **Execution:** The script will connect to each valid target in the file and display the output.

## Recent Improvements

The version in this workspace has been enhanced with:
- **File Input Support:** Dynamically load targets from an external file instead of editing the code.
- **Stability Fix:** Added error handling to prevent the script from crashing if one of the bots is offline.
- **Improved Logic:** Refactored functions for better modularity and testability.

## Security Warning

**Important:** This tool is for educational and authorized testing purposes only. 
- **Credentials:** Storing passwords in plain text in a file is insecure. Protect your target files.
- **Authorization:** Only use this tool on systems you own or have explicit permission to test. Unauthorized access is illegal.
