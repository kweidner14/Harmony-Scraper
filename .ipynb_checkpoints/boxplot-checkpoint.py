# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Author(s): Kyle Weidner
# Description: A Cryptocurrency web scraper

from scraper import *
import matplotlib.pyplot as plt
import statistics as stats

volumes_range = (max(harmony_volumes)) - (min(harmony_volumes))
volumes_labels = [str(int((i/10*volumes_range + min(harmony_volumes))/1000)) for i in range(0, 11, 2)]
#
volumes_normalized = min_max(harmony_volumes, min(harmony_volumes), max(harmony_volumes))
plt.boxplot(volumes_normalized)
median = stats.median(harmony_volumes)
max_value = max(harmony_volumes)
print(plt.annotate(str(max_value), xy=(1, max_value)))
print(plt.annotate(str(median), xy=(1, median)))

axes = plt.gca()
axes.spines['right'].set_visible(False)
axes.spines['top'].set_visible(False)
axes.set_yticks([i/10 for i in range(0, 11, 2)])
axes.set_yticklabels(volumes_labels)
axes.set_xticklabels(["Harmony One"])
plt.ylabel('Daily Trade Volume')
plt.show()
