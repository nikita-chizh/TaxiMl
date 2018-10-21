import numpy as np
import pandas as pd
import os
dpath = "/home/nikita/PycharmProjects/taxi/raw_data/yellow_tripdata_2016-05.csv"
df = pd.read_csv(dpath)
cols = df.columns.values
# ['VendorID' 'tpep_pickup_datetime' 'tpep_dropoff_datetime'
#  'passenger_count' 'trip_distance' 'pickup_longitude' 'pickup_latitude'
#  'RatecodeID' 'store_and_fwd_flag' 'dropoff_longitude' 'dropoff_latitude'
#  'payment_type' 'fare_amount' 'extra' 'mta_tax' 'tip_amount'
#  'tolls_amount' 'improvement_surcharge' 'total_amount']

ny_long = (-74.25559, -73.70001)
ny_lat = (40.49612, 40.91553)

def pridicate(x):
    fcond = x["tpep_pickup_datetime"] != x["tpep_dropoff_datetime"]
    scond = x["passenger_count"] != 0
    tcond = x["trip_distance"] != 0
    frcond = (ny_long[0] < x["pickup_longitude"] < ny_long[1]) and (ny_lat[0] < x["pickup_latitude"] < ny_lat[1])
    return fcond and scond and tcond and frcond

df = df[df.apply(pridicate, axis=1)]
#
spath = "/home/nikita/PycharmProjects/taxi/processed_data/"
df.to_csv(spath + '201605_filteredPYTHON.csv')
#####
# df = df[['tpep_pickup_datetime', 'pickup_longitude', 'pickup_latitude']]
# df.to_csv(spath + '201605_filteredHELP.csv')

