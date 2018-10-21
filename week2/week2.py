#
dpath = "/home/nikita/PycharmProjects/taxi/raw_data/regions.csv"
f = open(dpath)
l = f.readline()
poligons = []
centers = []
for l in f:
    row = l.split(";")
    for i in range(len(row)):
        row[i] = float(row[i])
    poligon = []
    poligon.append((row[3], row[1]))
    poligon.append((row[4], row[1]))
    poligon.append((row[4], row[2]))
    poligon.append((row[3], row[2]))
    poligon.append((row[3], row[1]))
    poligons.append(poligon)
    center = ((row[3] + row[4]) / 2, (row[1] + row[2]) / 2)
    centers.append(center)

import numpy as np
import pandas as pd
import os
from collections import Counter

dpath = "/home/nikita/PycharmProjects/taxi/processed_data/TwoDstat.csv"
twoD = pd.read_csv(dpath, index_col="Zone")
cellSum = twoD.sum(axis=1)
points = None

for i,v in cellSum.iteritems():
    if v != 0:
        new_points = np.zeros(shape=(v, 2))
        for n in range(v):
            new_points[n] = centers[i]
        if points is None:
            points = new_points
        else:
            points = np.concatenate((points, new_points), axis=0)
