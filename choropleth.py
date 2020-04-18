import os
import json
import pandas as pd
import folium

# state_geo = os.path.join('/home/aditi/Documents/IAT814/Project/', 'ca_fsa.json')
# # state_geo = json.loads('/home/aditi/Documents/IAT814/Project/ca_fsa.json')
#
#
# with open(state_geo, 'r') as j:
#      contents = json.loads(j.read())
# print(contents["features"][0]["properties"]["CFSAUID"])
# # print(state_geo["feature"]["properties"])
# df = os.path.join('/home/aditi/Documents/IAT814/Project/', 'HousePricePerFSA1.csv')
# state_data = pd.read_csv(df)
# print(state_data)
# m = folium.Map(location=[49.2019849, -123.10599847227], zoom_start=11)
# m.choropleth(
#     geo_data=state_geo,
#     name='choropleth',
#     data=state_data,
#     columns=['FSA', 'CURRENT_HOUSE_PRICE'],
#     key_on='feature.properties.CFSAUID',
#     fill_color='Reds',
#     fill_opacity=0.7,
#     line_opacity=0.4,
#     legend_name='House Price'
# )
#
# folium.LayerControl().add_to(m)
#feature
# m.save('/home/aditi/Documents/IAT814/Project/houseprice1.html')

import plotly.express as px

# fig = px.choropleth_mapbox(state_data, geojson=contents, color="CURRENT_HOUSE_PRICE",
#                            locations="FSA", featureidkey="properties.CFSAUID",
#                            center={"lat": 49.2519849, "lon": -123.10599847227},
#                            mapbox_style="carto-positron",
#                            color_continuous_scale=px.colors.sequential.Mint,
#                          # color_continuous_scale=[(0, "red"), (0.5, "green"), (1, "blue")],
#                            zoom=11)
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fsa_geo = os.path.join('/home/aditi/Documents/IAT814/Project/', 'ca_fsa.json')
with open(fsa_geo, 'r') as j:
    contents = json.loads(j.read())

data = pd.read_csv('/home/aditi/Documents/IAT814/Project/HousePricePerFSA' + str(1970) + '.csv')

fig = px.choropleth_mapbox(data, geojson=contents, color="CURRENT_HOUSE_PRICE",
                           locations="FSA", featureidkey="properties.CFSAUID",
                           center={"lat": 49.2519849, "lon": -123.10599847227},
                           mapbox_style="carto-positron",
                           color_continuous_scale=px.colors.sequential.Mint,
                           # color_continuous_scale=[(0, "red"), (0.5, "green"), (1, "blue")],
                           zoom=11)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
######################################################################
#
# state_geo = os.path.join('/home/aditi/Documents/IAT814/Project/', 'ca_fsa.json')
#
# state_unemployment = os.path.join('/home/aditi/Documents/IAT814/Project/', 'HousePricePerFSA2.csv')
# state_data = pd.read_csv(state_unemployment)
#
# m = folium.Map(location=[49.2019849, -123.10599847227], zoom_start=11)
# m.choropleth(
#     geo_data=state_geo,
#     name='choropleth',
#     data=state_data,
#     columns=['FSA', 'CURRENT_HOUSE_PRICE'],
#     key_on='feature.properties.CFSAUID',
#     fill_color='Reds',
#     fill_opacity=0.7,
#     line_opacity=0.4,
#     legend_name='House Price'
# )
#
# folium.LayerControl().add_to(m)
#
# m.save('/home/aditi/Documents/IAT814/Project/houseprice2.html')
#
# ######################################################################
#
# state_geo = os.path.join('/home/aditi/Documents/IAT814/Project/', 'ca_fsa.json')
#
# state_unemployment = os.path.join('/home/aditi/Documents/IAT814/Project/', 'HousePricePerFSA3.csv')
# state_data = pd.read_csv(state_unemployment)
#
# m = folium.Map(location=[49.2019849, -123.10599847227], zoom_start=11)
# m.choropleth(
#     geo_data=state_geo,
#     name='choropleth',
#     data=state_data,
#     columns=['FSA', 'CURRENT_HOUSE_PRICE'],
#     key_on='feature.properties.CFSAUID',
#     fill_color='Reds',
#     fill_opacity=0.7,
#     line_opacity=0.4,
#     legend_name='House Price'
# )
#
# folium.LayerControl().add_to(m)
#
# m.save('/home/aditi/Documents/IAT814/Project/houseprice3.html')
#
# ######################################################################
#
# state_geo = os.path.join('/home/aditi/Documents/IAT814/Project/', 'ca_fsa.json')
#
# state_unemployment = os.path.join('/home/aditi/Documents/IAT814/Project/', 'HousePricePerFSA4.csv')
# state_data = pd.read_csv(state_unemployment)
#
# m = folium.Map(location=[49.2019849, -123.10599847227], zoom_start=11)
# m.choropleth(
#     geo_data=state_geo,
#     name='choropleth',
#     data=state_data,
#     columns=['FSA', 'CURRENT_HOUSE_PRICE'],
#     key_on='feature.properties.CFSAUID',
#     fill_color='Reds',
#     fill_opacity=0.7,
#     line_opacity=0.4,
#     legend_name='House Price'
# )
#
# folium.LayerControl().add_to(m)
#
# m.save('/home/aditi/Documents/IAT814/Project/houseprice4.html')
#
# ######################################################################
#
# state_geo = os.path.join('/home/aditi/Documents/IAT814/Project/', 'ca_fsa.json')
#
# state_unemployment = os.path.join('/home/aditi/Documents/IAT814/Project/', 'HousePricePerFSA5.csv')
# state_data = pd.read_csv(state_unemployment)
#
# m = folium.Map(location=[49.2019849, -123.10599847227], zoom_start=11)
# m.choropleth(
#     geo_data=state_geo,
#     name='choropleth',
#     data=state_data,
#     columns=['FSA', 'CURRENT_HOUSE_PRICE'],
#     key_on='feature.properties.CFSAUID',
#     fill_color='Reds',
#     fill_opacity=0.7,
#     line_opacity=0.4,
#     legend_name='House Price'
# )
#
# folium.LayerControl().add_to(m)
#
# m.save('/home/aditi/Documents/IAT814/Project/houseprice5.html')
#
# ######################################################################
#
# state_geo = os.path.join('/home/aditi/Documents/IAT814/Project/', 'ca_fsa.json')
#
# state_unemployment = os.path.join('/home/aditi/Documents/IAT814/Project/', 'HousePricePerFSA6.csv')
# state_data = pd.read_csv(state_unemployment)
#
# m = folium.Map(location=[49.2019849, -123.10599847227], zoom_start=11)
# m.choropleth(
#     geo_data=state_geo,
#     name='choropleth',
#     data=state_data,
#     columns=['FSA', 'CURRENT_HOUSE_PRICE'],
#     key_on='feature.properties.CFSAUID',
#     fill_color='Reds',
#     fill_opacity=0.7,
#     line_opacity=0.4,
#     legend_name='House Price'
# )
#
# folium.LayerControl().add_to(m)
#
# m.save('/home/aditi/Documents/IAT814/Project/houseprice6.html')
