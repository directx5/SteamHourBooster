import os
import ctypes
import datetime
import subprocess

import steam.client

if not os.path.exists("config"):
    with open("config", "w", encoding="UTF-8") as config:
        config.write("username:password\ngameid,gameid,gameid,gameid,gameid,gameid")
        config.close()
    subprocess.call(["notepad", "config"])
else:
    if str(input("Do you want to open the config file? [Y/N]: ")).lower() == "y":
        subprocess.call(["notepad", "config"])

with open("config", "r", encoding="UTF-8") as f:
    config = f.read().split("\n")
    account = config[0].split(":")
    games = [int(x.strip()) for x in set(config[1].split(",")) if x.strip().isdigit()]

os.system("title Steam Hour Booster")
client = steam.client.SteamClient()
client.cli_login(*account)
client.change_status(persona_state=1)
client.games_played(games)
os.system("cls")

start = datetime.datetime.now()
while True:
    if ctypes.windll.user32.GetAsyncKeyState(0x1B):
        break
    else:
        current_time = str(datetime.datetime.now() - start).split(".")[0]
        os.system(f"title Steam Hour Booster - {client.user.name} - {current_time}")
        print(f"\r[Steam Hour Booster] -> Username: [{client.user.name}] | Boosting For: [{current_time}]", end="")

client.logout()
client.disconnect()
