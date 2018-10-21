import pandas as pd
import folium
import json

res_json_dict = {
    "type": "FeatureCollection",
    "features": []
}

dpath = "/home/nikita/PycharmProjects/taxi/raw_data/regions.csv"
f = open(dpath)
l = f.readline()
features = []

for l in f:
    row = l.split(";")
    f = {
        "type": "Feature",
        "id": "test",
        "properties": {
            "name": "test"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": []
        }
    }
    f["id"] = int(row[0])
    for i in range(len(row)):
        row[i] = float(row[i])
    coordinates = []
    coordinates.append([row[1], row[3]])
    coordinates.append([row[1], row[4]])
    coordinates.append([row[2], row[4]])
    coordinates.append([row[2], row[3]])
    f["geometry"]["coordinates"] = [coordinates]
    features.append(f)

res_json_dict["features"] = features
res_json = json.dumps(res_json_dict)
resfile = "NYheo.json"
f = open(resfile, 'w')
f.write(res_json)
