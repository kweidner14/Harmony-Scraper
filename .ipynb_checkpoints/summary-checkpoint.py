from scraper import *
import numpy as np

print("*** Summary Statistics ***")
print(f'Volumes Range: [{np.min(harmony_volumes)}, {np.max(harmony_volumes)}]')
print('Volumes Mean: {:.2f}'.format(np.mean(harmony_volumes)))
print('Volumes Median: {:.2f}'.format(np.median(harmony_volumes)))
print('Volumes STD: {:.2f}'.format(np.std(harmony_volumes)))
print(f'Price Range: [{np.min(harmony_daily_prices)}, {np.max(harmony_daily_prices)}]')
print('Price Mean: {:.2f}'.format(np.mean(harmony_daily_prices)))
print('Price Median: {:.2f}'.format(np.median(harmony_daily_prices)))
print('Price STD: {:.2f}'.format(np.std(harmony_daily_prices)))
