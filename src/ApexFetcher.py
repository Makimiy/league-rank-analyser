import time
import requests
import pandas as pd
import os
from dotenv import load_dotenv
# masters api url: "https://euw1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key="
# grandmaster api url: "https://euw1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key="
# chall api url:  "https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key="
load_dotenv()

api_key = os.getenv("api_key")
api_url = "https://euw1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key=" + api_key
all_data = []

def get_summoner(puuid):
    time.sleep(1.2)
    api_url = (
        "https://europe.api.riotgames.com/riot/account/v1/accounts/"
        + "by-puuid/" + puuid
        + "?api_key=" + api_key
    )
    summoner_response = requests.get(api_url)
    summoner = summoner_response.json()

    if summoner_response.status_code != 200:
        print(f"ERROR code: {list_response.status_code}")

    name = summoner["gameName"]
    tag = summoner["tagLine"]
    return name + "#" + tag
    
list_response = requests.get(api_url)

if list_response.status_code != 200:
    print(f"ERROR code: {list_response.status_code}")

list = list_response.json()

for entries in list["entries"]:
    print(entries["leaguePoints"])
    puuid = entries["puuid"]
    player = get_summoner(puuid)

    all_data.append({
        "lp": entries["leaguePoints"],
        "wins": entries["wins"],
        "losses": entries["losses"],
        "player": player,
        "puuid": puuid
    })

df = pd.DataFrame(data=all_data)
df.to_csv("GrandmasterEUW1.csv", index=False)