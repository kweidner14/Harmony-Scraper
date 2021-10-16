# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Author(s): Kyle Weidner
# Description: A Cryptocurrency web scraper

from scraper import *
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

import numpy as np

harmony_daily_prices.reverse()
dates.reverse()
plt.plot(dates, harmony_daily_prices)
plt.title("Harmony Price Chart (90 days)")
plt.xlabel("Dates")
plt.ylabel("Value in $")
plt.show()
