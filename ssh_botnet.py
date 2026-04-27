#!/usr/bin/env python3
# Coded by CyberCommands
import os
import optparse
from pexpect import pxssh

os.system('cls' if os.name == 'nt' else 'clear')
print('''
======================================
THIS IS A SIMPLE SSH BOT CONTROL UNIT.
--------------------------------------
        Coded by CyberCommands
======================================''')

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
    
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('\033[91m[-] Error Connecting \033[0m')
    
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before
    
def botnet_command(botnet, command):
    for client in botnet:
        if client.session:
            output = client.send_command(command)
            print('[*] Output from ' + client.host)
            print('\033[32m[+] \033[0m' +str(output, encoding='utf-8')+ '\n')
        else:
            print(f'[-] Skipping {client.host} due to connection failure.')

def add_client(botnet, host, user, password):
    client = Client(host, user, password)
    botnet.append(client)

def load_bots_from_file(botnet, file_path):
    if not os.path.exists(file_path):
        print(f"\033[91m[-] Le fichier {file_path} n'existe pas.\033[0m")
        return False
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split('-')
                if len(parts) == 3:
                    host, user, password = parts
                    add_client(botnet, host.strip(), user.strip(), password.strip())
                else:
                    print(f"\033[93m[!] Ligne ignorée (format incorrect) : {line}\033[0m")
        return True
    except Exception as e:
        print(f"\033[91m[-] Erreur lors de la lecture du fichier : {e}\033[0m")
        return False

if __name__ == "__main__":
    file_path = input("Chemin du fichier de cibles (format: host-user-password) >> ")
    Botnet = []
    
    if load_bots_from_file(Botnet, file_path):
        if len(Botnet) > 0:
            order = input("Commande à exécuter >> ")
            botnet_command(Botnet, order)
        else:
            print("\033[91m[-] Aucun bot valide chargé.\033[0m")