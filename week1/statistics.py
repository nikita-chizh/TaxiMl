import numpy as np
import pandas as pd
import os
from collections import Counter

dpath = "/home/nikita/PycharmProjects/taxi/processed_data/TwoDstat.csv"
data = pd.read_csv(dpath, index_col="Zone")
zeros = 0
for index, row in data.iterrows():
    c = Counter(row)
    zeros+=c[0]
    a = 1
print(zeros)
