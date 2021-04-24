import ctypes
import datetime
import msvcrt
import os
import time

import gevent
import steam.client
import steam.enums.common

with open("config", "r") as f:
    config = f.read().split("\n")
    account = config[0].split(":")
    games = list(map(int, [x.strip() for x in set(config[1].split(",")) if x.strip() != "" and x.strip().isdigit()]))

client = steam.client.SteamClient()
client.cli_login(account[0], account[1])
client.change_status(persona_state=1)
client.games_played(games)
os.system("title Steam Booster")
os.system("cls")

start = datetime.datetime.now()
while True:
    if ctypes.windll.user32.GetAsyncKeyState(0x1B):
        time.sleep(0.5)
        break
    else:
        sliced = str(datetime.datetime.now() - start).split(":")
        current_time = f"{sliced[0]}.{sliced[1]}.{sliced[2].split('.')[0]}"
        os.system(f"title Steam Booster - [{client.username}] - [{current_time}]")
        print(f"\r[Steam Booster] -> Username: [{client.username}] | Boosting For: [{current_time}]", end="")
        gevent.sleep(0.1)

client.logout()
client.disconnect()
