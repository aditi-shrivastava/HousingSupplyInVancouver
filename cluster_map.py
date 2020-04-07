import statistics
import folium
import pandas as pd
from operator import add
from folium.plugins import MarkerCluster


def clustermap():
    df = pd.read_csv('/home/aditi/Documents/IAT814/Project/non-market-housing.csv', sep=';')

    df = df[~df['Geom'].isnull()]
    split1 = df['Geom'].str.split(r'\[(.*?)\]', expand=True)
    df['coord'] = split1[1]

    split2 = df['coord'].str.split(',', expand=True)
    df['long'] = split2[0]
    df['lat'] = split2[1]
    df.drop(['coord'], axis=1)

    df1 = df[(df['Occupancy Year'] <= 1970)]
    df2 = df[(df['Occupancy Year'] <= 1980)]
    df3 = df[(df['Occupancy Year'] <= 1990)]
    df4 = df[(df['Occupancy Year'] <= 2000)]
    df5 = df[(df['Occupancy Year'] <= 2010)]
    df6 = df[(df['Occupancy Year'] <= 2019)]

    comm_df = pd.read_csv('/home/aditi/Documents/IAT814/Project/community-centres.csv', sep=';')
    split1 = comm_df['Geom'].str.split(r'\[(.*?)\]', expand=True)
    comm_df['coord'] = split1[1]

    split2 = comm_df['coord'].str.split(',', expand=True)
    comm_df['long'] = split2[0]
    comm_df['lat'] = split2[1]
    comm_df.drop(['coord'], axis=1)

    lat_list_comm = comm_df['lat'].tolist()
    lat_list_comm = [float(i) for i in lat_list_comm]

    long_list_comm = comm_df['long'].tolist()
    long_list_comm = [float(i) for i in long_list_comm]

    address_comm = comm_df['ADDRESS'].tolist()
    name_comm = comm_df['NAME'].tolist()
    """""""""""""""""""""""""""""""""""""""""""""""
    CLUSTER MAP 1
    """""""""""""""""""""""""""""""""""""""""""""""
    df_seniors = df1[df1['Clientele - Seniors'] != 0]
    lat_list_seniors = df_seniors['lat'].tolist()
    lat_list_seniors = [float(i) for i in lat_list_seniors]

    long_list_seniors = df_seniors['long'].tolist()
    long_list_seniors = [float(i) for i in long_list_seniors]

    units_s = df_seniors['Clientele - Seniors'].tolist()
    address_s = df_seniors['Address'].tolist()
    operator_s = df_seniors['Operator'].tolist()
    year_s = df_seniors['Occupancy Year'].tolist()

    df_others = df1[df1['Clientele - Seniors'] == 0]
    lat_list_others = df_others['lat'].tolist()
    lat_list_others = [float(i) for i in lat_list_others]

    long_list_others = df_others['long'].tolist()
    long_list_others = [float(i) for i in long_list_others]

    units_o = list(map(add, df_others['Clientele- Families'].tolist(), df_others['Clientele - Other'].tolist()))
    address_o = df_others['Address'].tolist()
    operator_o = df_others['Operator'].tolist()
    year_o = df_others['Occupancy Year'].tolist()

    mean_lat = statistics.mean(lat_list_others)
    mean_long = statistics.mean(long_list_others)

    map_1 = folium.Map(location=[mean_lat, mean_long], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(map_1)

    for k in range(len(lat_list_seniors)):
        location = lat_list_seniors[k], long_list_seniors[k]
        popup = '<b>SENIORS <br><br>Number of units: </b>' + str(units_s[k]) + ' <br> <b>Address: </b>  ' + \
                address_s[k] + '<br>' + '<b>Operator: </b>' + operator_s[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_s[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='red')).add_to(marker_cluster)

    for k in range(len(lat_list_others)):
        location = lat_list_others[k], long_list_others[k]

        popup = '<b>FAMILIES AND OTHERS <br><br>Number of units: </b>' + str(units_o[k]) + ' <br> <b>Address: </b>  ' + \
                address_o[k] + '<br>' + '<b>Operator: </b>' + operator_o[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_o[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='blue')).add_to(marker_cluster)

        # for k in range(len(lat_list_comm)):
        #     location = lat_list_comm[k], long_list_comm[k]
        #
        #     popup = '<b>COMMUNITY CENTRE <br><br></b>' + ' <b>Name: </b>'+ name_comm[k]+' <br><b>Address: </b>  ' + \
        #             address_comm[k]
        #
        #     folium.Marker(
        #         location=location,
        #         clustered_marker=True,
        #         popup=folium.Popup(popup, max_width=300, min_width=300),
        #         icon=folium.Icon(color='green')).add_to(marker_cluster)

    map_1.save('/home/aditi/Documents/IAT814/Project/map_1.html')

    """""""""""""""""""""""""""""""""""""""""""""""
    CLUSTER MAP 2
    """""""""""""""""""""""""""""""""""""""""""""""
    df_seniors = df2[df2['Clientele - Seniors'] != 0]
    lat_list_seniors = df_seniors['lat'].tolist()
    lat_list_seniors = [float(i) for i in lat_list_seniors]

    long_list_seniors = df_seniors['long'].tolist()
    long_list_seniors = [float(i) for i in long_list_seniors]

    units_s = df_seniors['Clientele - Seniors'].tolist()
    address_s = df_seniors['Address'].tolist()
    operator_s = df_seniors['Operator'].tolist()
    year_s = df_seniors['Occupancy Year'].tolist()

    df_others = df2[df2['Clientele - Seniors'] == 0]
    lat_list_others = df_others['lat'].tolist()
    lat_list_others = [float(i) for i in lat_list_others]

    long_list_others = df_others['long'].tolist()
    long_list_others = [float(i) for i in long_list_others]

    units_o = list(map(add, df_others['Clientele- Families'].tolist(), df_others['Clientele - Other'].tolist()))
    address_o = df_others['Address'].tolist()
    operator_o = df_others['Operator'].tolist()
    year_o = df_others['Occupancy Year'].tolist()

    mean_lat = statistics.mean(lat_list_others)
    mean_long = statistics.mean(long_list_others)

    map_2 = folium.Map(location=[mean_lat, mean_long], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(map_2)

    for k in range(len(lat_list_seniors)):
        location = lat_list_seniors[k], long_list_seniors[k]
        popup = '<b>SENIORS <br><br>Number of units: </b>' + str(units_s[k]) + ' <br> <b>Address: </b>  ' + \
                address_s[k] + '<br>' + '<b>Operator: </b>' + operator_s[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_s[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='red')).add_to(marker_cluster)

    for k in range(len(lat_list_others)):
        location = lat_list_others[k], long_list_others[k]

        popup = '<b>FAMILIES AND OTHERS <br><br>Number of units: </b>' + str(units_o[k]) + ' <br> <b>Address: </b>  ' + \
                address_o[k] + '<br>' + '<b>Operator: </b>' + operator_o[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_o[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='blue')).add_to(marker_cluster)

    map_2.save('/home/aditi/Documents/IAT814/Project/map_2.html')

    """""""""""""""""""""""""""""""""""""""""""""""
    CLUSTER MAP 3
    """""""""""""""""""""""""""""""""""""""""""""""
    df_seniors = df3[df3['Clientele - Seniors'] != 0]
    lat_list_seniors = df_seniors['lat'].tolist()
    lat_list_seniors = [float(i) for i in lat_list_seniors]

    long_list_seniors = df_seniors['long'].tolist()
    long_list_seniors = [float(i) for i in long_list_seniors]

    units_s = df_seniors['Clientele - Seniors'].tolist()
    address_s = df_seniors['Address'].tolist()
    operator_s = df_seniors['Operator'].tolist()
    year_s = df_seniors['Occupancy Year'].tolist()

    df_others = df3[df3['Clientele - Seniors'] == 0]
    lat_list_others = df_others['lat'].tolist()
    lat_list_others = [float(i) for i in lat_list_others]

    long_list_others = df_others['long'].tolist()
    long_list_others = [float(i) for i in long_list_others]

    units_o = list(map(add, df_others['Clientele- Families'].tolist(), df_others['Clientele - Other'].tolist()))
    address_o = df_others['Address'].tolist()
    operator_o = df_others['Operator'].tolist()
    year_o = df_others['Occupancy Year'].tolist()

    mean_lat = statistics.mean(lat_list_others)
    mean_long = statistics.mean(long_list_others)

    map_3 = folium.Map(location=[mean_lat, mean_long], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(map_3)

    for k in range(len(lat_list_seniors)):
        location = lat_list_seniors[k], long_list_seniors[k]
        popup = '<b>SENIORS <br><br>Number of units: </b>' + str(units_s[k]) + ' <br> <b>Address: </b>  ' + \
                address_s[k] + '<br>' + '<b>Operator: </b>' + operator_s[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_s[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='red')).add_to(marker_cluster)

    for k in range(len(lat_list_others)):
        location = lat_list_others[k], long_list_others[k]

        popup = '<b>FAMILIES AND OTHERS <br><br>Number of units: </b>' + str(units_o[k]) + ' <br> <b>Address: </b>  ' + \
                address_o[k] + '<br>' + '<b>Operator: </b>' + operator_o[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_o[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='blue')).add_to(marker_cluster)

    map_3.save('/home/aditi/Documents/IAT814/Project/map_3.html')

    """""""""""""""""""""""""""""""""""""""""""""""
    CLUSTER MAP 4
    """""""""""""""""""""""""""""""""""""""""""""""
    df_seniors = df4[df4['Clientele - Seniors'] != 0]
    lat_list_seniors = df_seniors['lat'].tolist()
    lat_list_seniors = [float(i) for i in lat_list_seniors]

    long_list_seniors = df_seniors['long'].tolist()
    long_list_seniors = [float(i) for i in long_list_seniors]

    units_s = df_seniors['Clientele - Seniors'].tolist()
    address_s = df_seniors['Address'].tolist()
    operator_s = df_seniors['Operator'].tolist()
    year_s = df_seniors['Occupancy Year'].tolist()

    df_others = df4[df4['Clientele - Seniors'] == 0]
    lat_list_others = df_others['lat'].tolist()
    lat_list_others = [float(i) for i in lat_list_others]

    long_list_others = df_others['long'].tolist()
    long_list_others = [float(i) for i in long_list_others]

    units_o = list(map(add, df_others['Clientele- Families'].tolist(), df_others['Clientele - Other'].tolist()))
    address_o = df_others['Address'].tolist()
    operator_o = df_others['Operator'].tolist()
    year_o = df_others['Occupancy Year'].tolist()

    mean_lat = statistics.mean(lat_list_others)
    mean_long = statistics.mean(long_list_others)

    map_4 = folium.Map(location=[mean_lat, mean_long], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(map_4)

    for k in range(len(lat_list_seniors)):
        location = lat_list_seniors[k], long_list_seniors[k]
        popup = '<b>SENIORS <br><br>Number of units: </b>' + str(units_s[k]) + ' <br> <b>Address: </b>  ' + \
                address_s[k] + '<br>' + '<b>Operator: </b>' + operator_s[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_s[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='red')).add_to(marker_cluster)

    for k in range(len(lat_list_others)):
        location = lat_list_others[k], long_list_others[k]

        popup = '<b>FAMILIES AND OTHERS <br><br>Number of units: </b>' + str(units_o[k]) + ' <br> <b>Address: </b>  ' + \
                address_o[k] + '<br>' + '<b>Operator: </b>' + operator_o[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_o[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='blue')).add_to(marker_cluster)

    map_4.save('/home/aditi/Documents/IAT814/Project/map_4.html')

    """""""""""""""""""""""""""""""""""""""""""""""
    CLUSTER MAP 5
    """""""""""""""""""""""""""""""""""""""""""""""
    df_seniors = df5[df5['Clientele - Seniors'] != 0]
    lat_list_seniors = df_seniors['lat'].tolist()
    lat_list_seniors = [float(i) for i in lat_list_seniors]

    long_list_seniors = df_seniors['long'].tolist()
    long_list_seniors = [float(i) for i in long_list_seniors]

    units_s = df_seniors['Clientele - Seniors'].tolist()
    address_s = df_seniors['Address'].tolist()
    operator_s = df_seniors['Operator'].tolist()
    year_s = df_seniors['Occupancy Year'].tolist()

    df_others = df5[df5['Clientele - Seniors'] == 0]
    lat_list_others = df_others['lat'].tolist()
    lat_list_others = [float(i) for i in lat_list_others]

    long_list_others = df_others['long'].tolist()
    long_list_others = [float(i) for i in long_list_others]

    units_o = list(map(add, df_others['Clientele- Families'].tolist(), df_others['Clientele - Other'].tolist()))
    address_o = df_others['Address'].tolist()
    operator_o = df_others['Operator'].tolist()
    year_o = df_others['Occupancy Year'].tolist()

    mean_lat = statistics.mean(lat_list_others)
    mean_long = statistics.mean(long_list_others)

    map_5 = folium.Map(location=[mean_lat, mean_long], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(map_5)

    for k in range(len(lat_list_seniors)):
        location = lat_list_seniors[k], long_list_seniors[k]
        popup = '<b>SENIORS <br><br>Number of units: </b>' + str(units_s[k]) + ' <br> <b>Address: </b>  ' + \
                address_s[k] + '<br>' + '<b>Operator: </b>' + operator_s[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_s[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='red')).add_to(marker_cluster)

    for k in range(len(lat_list_others)):
        location = lat_list_others[k], long_list_others[k]

        popup = '<b>FAMILIES AND OTHERS <br><br>Number of units: </b>' + str(units_o[k]) + ' <br> <b>Address: </b>  ' + \
                address_o[k] + '<br>' + '<b>Operator: </b>' + operator_o[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_o[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='blue')).add_to(marker_cluster)

    map_5.save('/home/aditi/Documents/IAT814/Project/map_5.html')

    """""""""""""""""""""""""""""""""""""""""""""""
    CLUSTER MAP 6
    """""""""""""""""""""""""""""""""""""""""""""""
    df_seniors = df6[df6['Clientele - Seniors'] != 0]
    lat_list_seniors = df_seniors['lat'].tolist()
    lat_list_seniors = [float(i) for i in lat_list_seniors]

    long_list_seniors = df_seniors['long'].tolist()
    long_list_seniors = [float(i) for i in long_list_seniors]

    units_s = df_seniors['Clientele - Seniors'].tolist()
    address_s = df_seniors['Address'].tolist()
    operator_s = df_seniors['Operator'].tolist()
    year_s = df_seniors['Occupancy Year'].tolist()

    df_others = df6[df6['Clientele - Seniors'] == 0]
    lat_list_others = df_others['lat'].tolist()
    lat_list_others = [float(i) for i in lat_list_others]

    long_list_others = df_others['long'].tolist()
    long_list_others = [float(i) for i in long_list_others]

    units_o = list(map(add, df_others['Clientele- Families'].tolist(), df_others['Clientele - Other'].tolist()))
    address_o = df_others['Address'].tolist()
    operator_o = df_others['Operator'].tolist()
    year_o = df_others['Occupancy Year'].tolist()

    mean_lat = statistics.mean(lat_list_others)
    mean_long = statistics.mean(long_list_others)

    map_6 = folium.Map(location=[mean_lat, mean_long], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(map_6)

    for k in range(len(lat_list_seniors)):
        location = lat_list_seniors[k], long_list_seniors[k]
        popup = '<b>SENIORS <br><br>Number of units: </b>' + str(units_s[k]) + ' <br> <b>Address: </b>  ' + \
                address_s[k] + '<br>' + '<b>Operator: </b>' + operator_s[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_s[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='red')).add_to(marker_cluster)

    for k in range(len(lat_list_others)):
        location = lat_list_others[k], long_list_others[k]

        popup = '<b>FAMILIES AND OTHERS <br><br>Number of units: </b>' + str(units_o[k]) + ' <br> <b>Address: </b>  ' + \
                address_o[k] + '<br>' + '<b>Operator: </b>' + operator_o[
                    k] + '<br><b>Year when this was initially occupied: </b>' + str(year_o[k])

        folium.Marker(
            location=location,
            clustered_marker=True,
            popup=folium.Popup(popup, max_width=300, min_width=300),
            icon=folium.Icon(color='blue')).add_to(marker_cluster)

    map_6.save('/home/aditi/Documents/IAT814/Project/map_6.html')


if __name__ == '__main__':
    clustermap()
