# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Author(s): Kyle Weidner
# Description: A Cryptocurrency web scraper

from bs4 import BeautifulSoup
import requests
import csv


def min_max(data, mins, maxs, interval=(0, 1)):
    return [int(((data[i] - mins) / (maxs - mins) * (interval[1] - interval[0]) + interval[0]) * 100000) / 100000 for i in range(len(data))]


HARMONY_URL = "https://www.coingecko.com/en/coins/harmony/historical_data/usd?end_date=2021-09-25&start_date=2021-06-27#panel"

harmony = requests.get(HARMONY_URL)
h_soup = BeautifulSoup(harmony.content, 'html.parser')

harmony_daily_prices = []
harmony_volumes = []
dates = []

# row_data contains the <tr> for each day
row_data = h_soup.find_all('tr')

# We skip the first two rows because we do not need that data
for r in row_data[2:]:
    dates.append(str(r.findChildren()[0].get_text().strip()))
    open_price = float(r.findChildren()[3].get_text().strip().replace('$', ''))
    close_price = float(r.findChildren()[4].get_text().strip().replace('$', ''))
    harmony_daily_prices.append(round((open_price + close_price) / 2, 4))
    harmony_volumes.append(int(r.findChildren()[2].get_text().strip().replace("\n", "").replace("$", "").replace(",", "")))

with open('volumes.csv', 'w+', encoding='UTF8', newline='\n') as f:
    writer = csv.writer(f, delimiter=',')
    f.writelines(str(harmony_volumes))
