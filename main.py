import os
import requests
import time
import socket

from colorama import Fore
from requests.exceptions import ConnectionError, HTTPError, Timeout, RequestException

directories_path = r"directories directory"
subdomains_path = r"subdomains directory"

def dirfuzz():
    url = input(f'{Fore.RED}[+]{Fore.RESET} URL to fuzz: ')
    print("")
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url

    with open(directories_path, 'r') as file:
            directories = file.readlines()
            for directory in directories:
                directory = directory.strip()
                response = requests.get(url + "/" + directory)
                try:
                    if response.status_code == 200:
                        print(f'{Fore.GREEN}[+]{Fore.RESET} Directory found: {url}/{directory}\n')
                except (ConnectionError, HTTPError, Timeout, RequestException, socket.gaierror) as e:
                    pass
                
def subdfuzz():
    url = input(f'{Fore.RED}[+]{Fore.RESET} URL to fuzz: ')
    print("")
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url

    with open(subdomains_path, 'r') as file:
        subdomains = file.readlines()
        for subdomain in subdomains:
            subdomain = subdomain.strip()
            full_url = f'https://{subdomain}.{url.split("://")[1]}'
            try:
                response = requests.get(full_url)
                if response.status_code == 200:
                    print(f'{Fore.GREEN}[+]{Fore.RESET} Directory found: {full_url}\n')
            except (ConnectionError, HTTPError, Timeout, RequestException, socket.gaierror) as e:
                pass


def main():
    os.system('cls')
    print(f'''{Fore.RED}
          
▓█████▄  ██▓ ██▀███    █████▒█    ██ ▒███████▒▒███████▒
▒██▀ ██▌▓██▒▓██ ▒ ██▒▓██   ▒ ██  ▓██▒▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░
░██   █▌▒██▒▓██ ░▄█ ▒▒████ ░▓██  ▒██░░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ 
░▓█▄   ▌░██░▒██▀▀█▄  ░▓█▒  ░▓▓█  ░██░  ▄▀▒   ░  ▄▀▒   ░
░▒████▓ ░██░░██▓ ▒██▒░▒█░   ▒▒█████▓ ▒███████▒▒███████▒
 ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░ ▒ ░   ░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒
 ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░ ░     ░░▒░ ░ ░ ░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒
 ░ ░  ░  ▒ ░  ░░   ░  ░ ░    ░░░ ░ ░ ░ ░ ░ ░ ░░ ░ ░ ░ ░
   ░     ░     ░               ░       ░ ░      ░ ░    
 ░                                   ░        ░        
                
{Fore.RED} > {Fore.RESET} Creator: https://github.com/Sxmpl3


''')
    
    print(f'{Fore.RED}[+]{Fore.RESET} 1. Directory Fuzzing\n')
    print(f'{Fore.RED}[+]{Fore.RESET} 2. Subdomain Fuzzing\n')
    print(f'{Fore.RED}[+]{Fore.RESET} 3. Exit\n')
    select = input(f"{Fore.RED}->{Fore.RESET} ")
    print("")

    if select == "1":
        dirfuzz()
        time.sleep(5)
    elif select == "2":
        subdfuzz()
        time.sleep(5)
    elif select == "3":
        exit()
    else:
        print(f"{Fore.RED}Invalid option\n")
        time.sleep(5)
        main()

if __name__ == "__main__":
    main()