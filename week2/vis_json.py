import pandas as pd
import numpy as np
import folium
import json

dpath = "/home/nikita/PycharmProjects/taxi/processed_data/TwoDstat.csv"
twoD = pd.read_csv(dpath, index_col="Zone")
d = twoD.sum(axis=1).values.reshape((twoD.shape[0], 1))
z = np.array(range(1, len(d) + 1)).reshape((len(d), 1))
dz = np.concatenate((z, d), axis=1)

data = pd.DataFrame(dz, columns=['Zone', 'Rides'])
#
geo_data = "/home/nikita/PycharmProjects/taxi/week2/NYheo.json"
# Initialize the map:
m = folium.Map(location=[40.738, -73.98],
                        zoom_start=10,)

# Add the color for the chloropleth:
m.choropleth(
    geo_data=geo_data,
    name='choropleth',
    data=data,
    columns=['Zone', 'Rides'],
    key_on='feature.id',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Rides number'
)
folium.LayerControl().add_to(m)
est = (40.7484, -73.9857)
folium.Marker(location=est, popup="Empire State Building").add_to(m)
# Save to html
m.save('AllRides.html')


