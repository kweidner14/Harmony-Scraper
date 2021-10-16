# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Author(s): Kyle Weidner
# Description: A Cryptocurrency web scraper

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date, timedelta


def min_max(data, mins, maxs, interval=(0, 1)):
    return [int(((data[i] - mins) / (maxs - mins) * (interval[1] - interval[0]) + interval[0]) * 100000) / 100000 for i in range(len(data))]


end_date = date.today()
start_date = end_date - timedelta(days=90)

HARMONY_URL = "https://www.coingecko.com/en/coins/harmony/historical_data/usd?end_date=" + str(end_date) + "&start_date=" + str(start_date) + "#panel"

harmony = requests.get(HARMONY_URL)
h_soup = BeautifulSoup(harmony.content, 'html.parser')

harmony_daily_prices = []
harmony_volumes = []
dates = []
open_prices = []
close_prices = []

# row_data contains the <tr> for each day
row_data = h_soup.find_all('tr')

# We skip the first two rows because we do not need that data
for r in row_data[2:]:
    dates.append(str(r.findChildren()[0].get_text().strip()))
    open_price = float(r.findChildren()[3].get_text().strip().replace('$', ''))
    open_prices.append(open_price)
    close_price = float(r.findChildren()[4].get_text().strip().replace('$', ''))
    close_prices.append(close_price)
    harmony_daily_prices.append(round((open_price + close_price) / 2, 4))
    harmony_volumes.append(int(r.findChildren()[2].get_text().strip().replace("\n", "").replace("$", "").replace(",", "")))

# with open('volumes.csv', 'w+', encoding='UTF8', newline='\n') as f:
#     writer = csv.writer(f, delimiter=',')
#     for v in harmony_volumes:
#         f.write(str(v) + '\n')
#
# with open('prices.csv', 'w+', encoding='UTF8', newline='\n') as f2:
#     writer2 = csv.writer(f, delimiter=',')
#     for p in harmony_daily_prices:
#         f2.write(str(p) + '\n')

dataset = pd.DataFrame(
    {"Dates": dates,
     "Open Price": open_prices,
     "Close Price": close_prices,
     "Daily Trade Volume": harmony_volumes
     }
)
dataset.to_csv('dataset.csv', encoding='UTF-8', index=False)

