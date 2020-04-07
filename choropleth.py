import os

import pandas as pd
import folium

# Load the shape of the zone (US states)
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
# You have to download this file and set the directory where you saved it
state_geo = os.path.join('/home/aditi/Documents/IAT814/Project/', 'ca_fsa.json')

# Load the unemployment value of each state
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
state_unemployment = os.path.join('/home/aditi/Documents/IAT814/Project/', 'HousePricePerFSA.csv')
state_data = pd.read_csv(state_unemployment)



# Initialize the map:
m = folium.Map(location=[49.2019849, -123.10599847227], zoom_start=10)

# Add the color for the chloropleth:
m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['FSA', 'CURRENT_HOUSE_PRICE'],
    key_on='feature.properties.CFSAUID',
    fill_color='RdPu',
    fill_opacity=0.7,
    line_opacity=0.4,
    legend_name='House Price'
)
folium.LayerControl().add_to(m)

# Save to html
m.save('/home/aditi/Documents/IAT814/Project/houseprice.html')
