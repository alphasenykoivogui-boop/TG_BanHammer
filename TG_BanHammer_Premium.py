pkg update && pkg upgrade -y
pkg install python python-pip git -y
pip install telethon colorama tqdm requests asyncio
git clone https://github.com/tonrepo/TG_BanHammer
cd TG_BanHammer
mkdir sessions
nano accounts.txt   # ajoute tes comptes (phone|api_id|api_hash)
python TG_BanHammer_Premium.py
