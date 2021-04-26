import ctypes
import datetime
import os
import subprocess
import steam.client

run = str(input("Do you want to open the config file? [Y/N]: "))
if run.lower() == "y":
    subprocess.call(["notepad", "config"])

with open("config", "r") as f:
    config = f.read().split("\n")
    account = dict(zip(["username", "password"], config[0].split(":")))
    games = [int(x.strip()) for x in set(config[1].split(",")) if x.strip().isdigit()]

os.system("title Steam Hour Booster")
client = steam.client.SteamClient()
client.cli_login(account["username"], account["password"])
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
