import ctypes
import datetime
import os
import subprocess

import steam.client

if not os.path.exists("config"):
    with open("config", "w", encoding="UTF-8") as config:
        config.write(f"username:password\n{('game_id,' * 10)[:-1]}")
    subprocess.call(["notepad", "config"])
else:
    if str(input("Do you want to open the config file? [Y/N]: ")).lower() == "y":
        subprocess.call(["notepad", "config"])

with open("config", "r", encoding="UTF-8") as f:
    config = f.read().split("\n")
    account = [x.strip() for x in config[0].split(":")[:2]]
    games = [int(c) for x in set(config[1].split(",")) if (c := x.strip()).isdigit()]

os.system("title Steam Hour Booster")
client = steam.client.SteamClient()
client.cli_login(*account)
client.games_played(games)
os.system("cls")

start = datetime.datetime.now()
while True:
    if ctypes.windll.user32.GetAsyncKeyState(0x1B):
        break
    else:
        current_time = str(datetime.datetime.now() - start).split(".")[0]
        print(f"\r[Steam Hour Booster] -> Username: [{client.user.name}] | Boosting For: [{current_time}]", end="")

client.logout()
client.disconnect()
