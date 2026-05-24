import time
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("api_key")
tiers = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"]
divisions = ["IV", "III", "II", "I"]
all_data = []

def output_status(tier, division, page_number, total):
    return print(f"League: {tier} | Division: {division} | "
                 f"Page: {page_number} | Total: {total}")

def output_total(tier, division, division_total):
    return print(f"The total for {tier} {division} is: {division_total}")

def append_dictionary(tier, division, division_total):
    all_data.append({
        "tier": tier,
        "division": division,
        "total": division_total
    })

# The standard "page" returns a list of 205 summoners with their data.
for tier in tiers:
    for division in divisions:
        page_number = 0
        total = 0
        while True:
            time.sleep(1.2)
            page_number += 1
            api_url = (
                "https://vn2.api.riotgames.com/lol/league/v4/entries" 
                + "/RANKED_SOLO_5x5/" + tier
                + "/"                 + division
                + "?page="            + str(page_number) 
                + "&api_key="         + api_key
            )

            response = requests.get(api_url)

            if response.status_code != 200:
                print(f"ERROR code: {response.status_code}")
               
            page = response.json()
            if len(page) == 0:
                division_total = total
                page_number = 0
                total = 0
                append_dictionary(tier, division, division_total)
                output_total(tier, division, division_total)
                break
            else:
                total += len(page)
                output_status(tier, division, page_number, total)

df = pd.DataFrame(data=all_data)
df.to_csv("LoLRanksVN2.csv", index=False)