# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Author(s): Kyle Weidner
# Description: A Cryptocurrency web scraper

from scraper import *
import matplotlib.pyplot as plt

counts, bins, _ = plt.hist(
    harmony_daily_prices,
    bins=[0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19, 0.21],
    rwidth=0.5
)
bins = [x + .01 for x in bins]
axes = plt.gca()
axes.set_xticks(bins)
axes.set_xticklabels(['0.05', '0.07', '0.09', '.11', '.13', '.15', '.17', '.19', '.21'])
plt.xlabel("Coin Price ($)")
plt.ylabel("Days at price")
plt.show()
