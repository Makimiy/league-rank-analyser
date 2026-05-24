from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import pandas as pd
import time
# 20/05/2026 - 11:00AM from page 11 to page 233 - Masters
# 20/05/2026 - 11:05AM from page 4 to page 11 - Grandmasters
# 20/05/2026 - 11:07AM from page 1 to page 4 - Challenger
file_path = "C:\\Program Files (x86)\\geckodriver.exe"
all_data = []

service = Service(executable_path=file_path)
driver = webdriver.Firefox(service=service)
start = 11
end = 233
for page in range(start, end):
    url = "https://op.gg/lol/leaderboards/tier?region=euw&page=" + str(page)
    driver.get(url)
    print(f"Page number: {page}")
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", class_ = "w-full table-fixed [&_caption]:hidden [&_tbody_tr:not(.ad)]:border-b [&_tbody_tr:not(.ad)]:border-b-gray-200 [&_tbody_tr:not(.ad):last-of-type]:border-0 [&_th]:font-normal [&_th]:box-border [&_th]:align-middle [&_tr:not(.ad)_th:first-of-type]:pl-3 [&_tr:not(.ad)_th:last-of-type]:pr-3 [&_td]:font-normal [&_td]:box-border [&_td]:align-middle [&_tr:not(.ad)_td]:p-1 [&_tr:not(.ad)_td:first-of-type]:pl-3 [&_tr:not(.ad)_td:last-of-type]:pr-3 [&_thead_th]:bg-gray-100 [&_thead_th]:h-8 [&_thead_th]:box-border [&_thead_th]:text-gray-400 [&_thead_th]:text-xs [&_thead_th]:whitespace-nowrap [&_thead_th]:p-0 [&_thead_th]:border-b [&_thead_th:not(.table-sort)]:border-gray-200 [&_tbody_th:not(.bg-gray-100)]:bg-gray-0 [&_tbody_tr:not(.ad)_td:not(.bg-gray-100)]:bg-gray-0 [&_tbody_tr:last-of-type_th]:border-0 [&_tbody_tr:last-of-type_td]:border-0 md:table-hover md:[&(.table-hover)_tbody_tr:hover_th]:bg-gray-100 md:[&(.table-hover)_tbody_tr:not(.ad):hover_td:not(.bg-gray-100)]:bg-gray-100 table-hover [&(.table-hover)_tbody_tr:hover_th]:bg-gray-100 [&(.table-hover)_tbody_tr:not(.ad):hover_td:not(.bg-gray-100)]:bg-gray-100 table-rounded [&(.table-rounded)_thead_th:first-of-type]:rounded-tl-sm [&(.table-rounded)_thead_th:last-of-type]:rounded-tr-sm [&(.table-rounded)_tbody_tr:last-of-type_td:first-of-type]:rounded-bl-sm [&(.table-rounded)_tbody_tr:last-of-type_td:last-of-type]:rounded-br-sm overflow-hidden text-xs md:rounded [&_thead_th]:px-1")
    rows = table.find_all("tr")
    for row in rows:
        summoner = row.find("div", class_ = "flex items-center")
        lp = row.select_one("div.text-gray-600:not(.hidden)")
        wins = row.find("span", class_ = "absolute left-1 top-1/2 z-10 -translate-y-1/2 whitespace-nowrap text-2xs text-white")
        losses = row.find("span", class_ = "absolute right-1 top-1/2 z-10 -translate-y-1/2 whitespace-nowrap text-2xs text-white")
        if summoner is not None:
            print(summoner.text + " | " + lp.text + " | " + wins.text + " | " + losses.text)
            win = int(wins.text.rstrip("W"))
            loss = int(losses.text.rstrip("L"))
            all_data.append({
                "lp": lp.text,
                "wins": win,
                "losses": loss,
                "player": summoner.text
            })

    df = pd.DataFrame(data=all_data)
    df.to_csv("MastersOPGGEUW1.csv", index=False)