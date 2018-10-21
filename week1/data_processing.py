import numpy as np
import pandas as pd
import os
from scipy.stats import binned_statistic_2d
newHZ = "/Users/nikita/PycharmProjects/TaxiTask/processed_data/AllMonth/m5_all1.csv"
oldHZ = "/Users/nikita/PycharmProjects/TaxiTask/processed_data/HoursZonesOLD.csv"
#
newF = open(newHZ)
oldF = open(oldHZ)
#
# num_linesOLD = sum(1 for line in oldF)
# num_linesNEW = sum(1 for line in newF)
# if(num_linesOLD != num_linesNEW):
#     print("LINES ERROR")
#     exit(1)
# print("OK")
#
newl = newF.readline()
oldl = oldF.readline()



tripid = 0
for oldl in oldF:
    newl = newF.readline()
    oldSplit = oldl.split(',')
    newSplit = newl.split(',')
    if(int(oldSplit[2]) != int(newSplit[2])):
        print("ZONE ERROR ID = " + str(tripid))
    hold = int(oldSplit[1])
    hnew = int(newSplit[1])
    if(hold != hnew - 2928):
        print("HOUR ERROR ID = " + str(tripid))
        break
    tripid+=1