import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import os,json

FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
CS = 'https://codepen.io/chriddyp/pen/bWLwgP.css'

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FA, CS])
server = app.server
app.config['suppress_callback_exceptions'] = True

df = pd.read_csv('data/BarCharts.csv')

trace1 = go.Bar(name='% Seniors Housing', x=df['Local Area'], y=df['Clientele - Seniors'], marker_color='Red')
trace2 = go.Bar(name='% Families and Others', x=df['Local Area'], y=df['NonSeniors'], marker_color='lightgreen')

trace3 = go.Bar(name='% Rented', x=df['Local Area'], y=df['Rented'])
trace4 = go.Bar(name='% Owned', x=df['Local Area'], y=df['Owned'])

fig1 = make_subplots(rows=1, cols=1,
                     shared_xaxes=True
                     )

fig1.append_trace(trace1, 1, 1)
fig1.append_trace(trace2, 1, 1)

fig1.update_layout(barmode='group',
                   title={
                       'text': "Distribution of Housing types in Vancouver",
                       'y': 0.9,
                       'x': 0.5,
                       'xanchor': 'center',
                       'yanchor': 'top',
                   },
                   width=1300,
                   height=550,
                   font=dict(
                       size=14,
                       color="black"
                   )
                   )

trace1 = go.Bar(name='Current House Price', x=df['Local Area'], y=df['CURRENT_HOUSE_PRICE'])
trace2 = go.Bar(name='% Seniors', x=df['Local Area'], y=df['SeniorsPerFSApercentage'])

fig2 = make_subplots(rows=2, cols=1,
                     shared_xaxes=True
                     )

fig2.append_trace(trace1, 1, 1)
fig2.append_trace(trace2, 2, 1)

fig2.update_layout(title={
    'text': "Distribution of Housing prices and Seniors",
    'y': 0.9,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top',
},
    width=780,
    height=700,
    font=dict(
        size=14,
        color="black"
    )
)

heatmap = pd.read_csv('data/BarCharts.csv')
fig_heatmap = go.Figure(data=go.Heatmap(
                   z=[heatmap['Clientele - Seniors'],heatmap['NonSeniors'],heatmap['OthersHousing']],
                   x=heatmap['Local Area'],
                   y=['% Senior Housing', '% Families Housing', '% Others'],
                    colorscale=px.colors.sequential.Bluyl,
                   hoverongaps = False))
fig_heatmap.update_layout(title={
                       'text': "Distribution of Housing types in Vancouver",
                       'x': 0.5,
                       'xanchor': 'center',
                       'yanchor': 'top',
                   },
                   width=1250,
                   height=550,
                   font=dict(
                       size=14,
                       color="black"
                   )
                   )
# fig_heatmap.show()
df1 = pd.read_csv('data/VanProperties.csv')

df1 = df1[df1['FSA'] == 'V5K']
df1 = df1['CATEGORY'].value_counts().reset_index()
fig3 = go.Figure(data=[go.Pie(labels=df1['index'], values=df1['CATEGORY'].value_counts(), hole=.3)])

navbar = dbc.Navbar(
    [
        html.Div(html.H1(children='Housing Supply In Vancouver',
                         style={
                             'text-align': 'center',
                             'color': 'white',
                             'font': 'Courier New'
                         }),
                 className="offset-by-one column ten columns"
                 )
    ],
    color="#4c4c4c",
)

slider = dbc.Container(
    [
        dbc.Row(
            html.Div(
                daq.Slider(
                    id='year',
                    min=1970,
                    max=2019,
                    size=600,
                    value=2000,
                    handleLabel={"showCurrentValue": True, "label": "Year"},
                    marks={str(year): str(year) for year in (1970, 1980, 1990, 2000, 2010, 2019)},
                    step=None
                ), style={"width": "2%", "display": "inline-block", "position": "relative",
                          "margin-top": "50px", "margin-bottom": "50px", "margin-left": "200px"}
            )
        )
    ]
)

map = dbc.Container(
    [
        dbc.Row(

            html.Div(
                dcc.Graph(id='mapoutput')
            ),
            style={"display": "inline-block", "position": "relative",
                   "margin-top": "20px", "margin-bottom": "20px",
                   "margin-left": "-130px"},
        ),
    ]
)

bar1 = dbc.Container(
    [
        dbc.Row(
            html.Div(
                dcc.Graph(figure=fig_heatmap)
            ),
            style={"display": "inline-block", "position": "relative",
                   "margin-top": "20px", "margin-bottom": "20px",
                   "margin-left": "-180px"},
        ),
    ]
)

subtitle = dbc.Container(
    [
        html.Div(
            html.H2(children='Compare 2 FSA',
                    style={
                        'text-align': 'center',
                        'color': 'black',
                        'font': 'Courier New'
                    }),
            className="offset-by-one column ten columns"
        )

    ]
)

subsection = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            html.Div(
                                (
                                    dcc.Dropdown(id='drop1',
                                                 options=[
                                                     {'label': 'Arbutus-Ridge', 'value': 'V6L'},
                                                     {'label': 'Downtown', 'value': 'V6Z'},
                                                     {'label': 'Dunbar-Southlands', 'value': 'V6S'},
                                                     {'label': 'Fairview', 'value': 'V6H'},
                                                     {'label': 'Grandview-Woodland', 'value': 'V5L'},
                                                     {'label': 'Hastings-Sunrise', 'value': 'V5K'},
                                                     {'label': 'Kensington-Cedar Cottage', 'value': 'V5N'},
                                                     {'label': 'Kerrisdale', 'value': 'V6P'},
                                                     {'label': 'Killarney', 'value': 'V5S'},
                                                     {'label': 'Kitsilano', 'value': 'V6J'},
                                                     {'label': 'Marpole', 'value': 'V5X'},
                                                     {'label': 'Mount Pleasant', 'value': 'V5T'},
                                                     {'label': 'Oakridge', 'value': 'V6M'},
                                                     {'label': 'Renfrew-Collingwood', 'value': 'V5M'},
                                                     {'label': 'Riley Park', 'value': 'V5V'},
                                                     {'label': 'South Cambie', 'value': 'V5Z'},
                                                     {'label': 'Strathcona', 'value': 'V6A'},
                                                     {'label': 'Sunset', 'value': 'V5W'},
                                                     {'label': 'Victoria-Fraserview', 'value': 'V5P'},
                                                     {'label': 'West End', 'value': 'V6E'},
                                                     {'label': 'West Point Grey', 'value': 'V6R'}

                                                 ],
                                                 value='V6P'
                                                 )
                                ), className="offset-by-four column four columns",
                                style={"display": "inline-block", "position": "relative",
                                       "width": "50%",
                                         "margin-left": "90px",
                                        "margin-right": "-40px",
                                       },
                            )

                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            html.Div(
                                (
                                    dcc.Dropdown(id='drop2',
                                                 options=[
                                                     {'label': 'Arbutus-Ridge', 'value': 'V6L'},
                                                     {'label': 'Downtown', 'value': 'V6Z'},
                                                     {'label': 'Dunbar-Southlands', 'value': 'V6S'},
                                                     {'label': 'Fairview', 'value': 'V6H'},
                                                     {'label': 'Grandview-Woodland', 'value': 'V5L'},
                                                     {'label': 'Hastings-Sunrise', 'value': 'V5K'},
                                                     {'label': 'Kensington-Cedar Cottage', 'value': 'V5N'},
                                                     {'label': 'Kerrisdale', 'value': 'V6P'},
                                                     {'label': 'Killarney', 'value': 'V5S'},
                                                     {'label': 'Kitsilano', 'value': 'V6J'},
                                                     {'label': 'Marpole', 'value': 'V5X'},
                                                     {'label': 'Mount Pleasant', 'value': 'V5T'},
                                                     {'label': 'Oakridge', 'value': 'V6M'},
                                                     {'label': 'Renfrew-Collingwood', 'value': 'V5M'},
                                                     {'label': 'Riley Park', 'value': 'V5V'},
                                                     {'label': 'South Cambie', 'value': 'V5Z'},
                                                     {'label': 'Strathcona', 'value': 'V6A'},
                                                     {'label': 'Sunset', 'value': 'V5W'},
                                                     {'label': 'Victoria-Fraserview', 'value': 'V5P'},
                                                     {'label': 'West End', 'value': 'V6E'},
                                                     {'label': 'West Point Grey', 'value': 'V6R'}

                                                 ],
                                                 value='V5L'
                                                 )
                                ), className="offset-by-four column four columns",
                                style={"display": "inline-block", "position": "relative",
                                       "width": "50%", "margin-left": "78px"
                                       },
                            )

                        ),
                    ]
                )
            ]
        )
    ]
)

bars = dbc.Container(
    dbc.Row(
        [
            dbc.Row(
                html.Div(
                    dcc.Graph(id='barNew_1')
                ),
                style={"height": "33.3%",
                       "display": "inline-block", "position": "relative",
                       # "margin-top": "20px","margin-bottom": "20px",
                       "margin-left": "-120px"
                       },
            ),
            dbc.Row(
                html.Div(
                    dcc.Graph(id='barNew_2')
                ), style={"height": "33.3%",
                          "display": "inline-block", "position": "relative",
                          # "margin-top": "20px","margin-bottom": "20px",
                          "margin-left": "-120px"
                          }
            ),
            dbc.Row(
                html.Div(
                    dcc.Graph(id='barNew_3')
                ), style={"height": "33.3%",
                          "display": "inline-block", "position": "relative",
                          # "margin-top": "20px","margin-bottom": "20px",
                          "margin-left": "-120px"
                          }
            )
        ]
    )
)

@app.callback(
    Output('mapoutput', 'figure'),
    [Input('year', 'value')])
def update_figure(year):

    fsa_geo = os.path.join('data/', 'ca_fsa.json')
    with open(fsa_geo, 'r') as j:
        contents = json.loads(j.read())
    data = pd.read_csv('data/HousePricePerFSA'+str(year)+'.csv')
    fig = px.choropleth_mapbox(data, geojson=contents, color="CURRENT_HOUSE_PRICE",
                               locations="FSA", featureidkey="properties.CFSAUID",
                               center={"lat": 49.2629849, "lon": -123.10599847227},
                               mapbox_style="carto-positron",
                               color_continuous_scale=px.colors.sequential.Mint,
                               hover_data=["Local Area"],
                               zoom=10.8)

    fig.update_layout(height=650, width=1300,
                      title={
                          'text': "Distribution of Average House Prices",
                          'x': 0.5,
                      },
                      font=dict(
                          size=14,
                          color="black"
                      ),
                      )
    return fig

@app.callback(
    Output('barNew_1', 'figure'),
    [Input('drop1', 'value'),
     Input('drop2', 'value')
     ])
def update_graph(drop1,drop2):
    df = pd.read_csv('data/VanProperties.csv')

    df1 = df[df['FSA'] == drop1]
    one = df1[df1['CATEGORY'].isin(['One Family Dwelling'])]
    one = one['CATEGORY'].value_counts().reset_index()
    if len(one['CATEGORY'].to_list()) == 0:
        one = [0]
    else:
        one = one['CATEGORY'].to_list()

    two = df1[df1['CATEGORY'].isin(['Two Family Dwelling'])]
    two = two['CATEGORY'].value_counts().reset_index()
    if len(two['CATEGORY'].to_list()) == 0:
        two = [0]
    else:
        two = two['CATEGORY'].to_list()

    mul = df1[df1['CATEGORY'].isin(['Multiple Family Dwelling'])]
    mul = mul['CATEGORY'].value_counts().reset_index()
    if len(mul['CATEGORY'].to_list()) == 0:
        mul = [0]
    else:
        mul = mul['CATEGORY'].to_list()

    list = one + two + mul

    sum1 = sum(list)

    if sum1 == 0:
        sum1 = 0.1

    for i in range(len(list)):
        list[i] = (list[i] * 100) / sum1

    # print(list)

    fig = go.Figure(
        data=[go.Bar(x=['1-Fam Dwell', '2-Fam Dwell', 'Multiple-Fam Dwell'], y=list, width=0.5, marker_color='#388E8E')])

    fig.update_layout(title={
        'text': "Distribution of Occupancy types",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
    },
        yaxis_title="Percentage",
        width=420,
        height=550,
        font=dict(
            size=14,
            color="black"
        ),
    )

    # fig.show()

    fig = make_subplots(rows=1, cols=2, shared_yaxes=True)

    fig.add_trace(
        go.Bar(x=['1-Fam Dwell', '2-Fam Dwell', 'Multiple-Fam Dwell'], y=list, width=0.5, marker_color='#388E8E'),
        row=1, col=1
    )

    df1 = df[df['FSA'] == drop2]
    one = df1[df1['CATEGORY'].isin(['One Family Dwelling'])]
    one = one['CATEGORY'].value_counts().reset_index()
    if len(one['CATEGORY'].to_list()) == 0:
        one = [0]
    else:
        one = one['CATEGORY'].to_list()

    two = df1[df1['CATEGORY'].isin(['Two Family Dwelling'])]
    two = two['CATEGORY'].value_counts().reset_index()
    if len(two['CATEGORY'].to_list()) == 0:
        two = [0]
    else:
        two = two['CATEGORY'].to_list()

    mul = df1[df1['CATEGORY'].isin(['Multiple Family Dwelling'])]
    mul = mul['CATEGORY'].value_counts().reset_index()
    if len(mul['CATEGORY'].to_list()) == 0:
        mul = [0]
    else:
        mul = mul['CATEGORY'].to_list()

    list = one + two + mul

    sum1 = sum(list)

    if sum1 == 0:
        sum1 = 0.1

    for i in range(len(list)):
        list[i] = (list[i] * 100) / sum1

    fig.add_trace(
        go.Bar(x=['1-Fam Dwell', '2-Fam Dwell', 'Multiple-Fam Dwell'], y=list, width=0.5, marker_color='#388E8E'),
        row=1, col=2
    )

    fig.update_layout(height=600, width=1200,
                      # title_text="Distribution of Occupancy types",
                      title={
                          'text': "Distribution of Occupancy types",
                          'y': 0.9,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top',
                      },
                    font=dict(
                            size=14,
                            color="black"
                        ),
                      showlegend=False)
    return fig



@app.callback(
    Output('barNew_2', 'figure'),
    [Input('drop1', 'value'),
     Input('drop2', 'value')
     ])
def update_graph(drop1,drop2):
    df = pd.read_csv('data/BarCharts.csv')
    df2 = df[df['FSA'] == drop1]

    rented = df2['Rented'].to_list()
    owned = df2['Owned'].to_list()
    list = rented + owned

    fig = make_subplots(rows=1, cols=2, shared_yaxes=True)

    fig.add_trace(
        go.Bar(x=['Rented', 'Owned'], y=list, width=[0.3, 0.3], marker_color='#388E8E'),
        row=1, col=1
    )

    df2 = df[df['FSA'] == drop2]

    rented = df2['Rented'].to_list()
    owned = df2['Owned'].to_list()
    list = rented + owned
    fig.add_trace(
        go.Bar(x=['Rented', 'Owned'], y=list, width=[0.3, 0.3], marker_color='#388E8E'),
        row=1, col=2
    )
    fig.update_layout(height=600, width=1200,
                      # title_text="Distribution of Occupancy types",
                      title={
                          'text': "Distribution of Ownership type",
                          'y': 0.9,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top',
                      },
                      font=dict(
                          size=14,
                          color="black"
                      ),
                      showlegend=False)
    return fig


@app.callback(
    Output('barNew_3', 'figure'),
    [Input('drop1', 'value'),
     Input('drop2', 'value')
     ])
def update_graph(drop1,drop2):
    df = pd.read_csv('data/AgeGroup.csv')
    df3 = df[~df['AgeGroup'].isin(['0'])]
    df3['per'] = (df3[drop1] * 100) / sum(df3[drop1])
    colors = ['#388E8E'] * 5
    fig = make_subplots(rows=1, cols=2, shared_yaxes=True)

    fig.add_trace(
        go.Bar(x=df3['AgeGroup'], y=df3['per'],width=0.6, marker_color=colors),
        row=1, col=1
    )

    df3 = df[~df['AgeGroup'].isin(['0'])]
    df3['per'] = (df3[drop2] * 100) / sum(df3[drop2])
    colors = ['#388E8E'] * 5

    fig.add_trace(
        go.Bar(x=df3['AgeGroup'], y=df3['per'],width=0.6, marker_color=colors),
        row=1, col=2
    )

    fig.update_layout(height=600, width=1200,
                      title={
                          'text': "Distribution of Age Group",
                          'y': 0.9,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top',
                      },
                      font=dict(
                          size=14,
                          color="black"
                      ),
                      showlegend=False)
    return fig


app.layout = html.Div([
    navbar,
    slider,
    map,
    bar1,
    subtitle,
    subsection,
    bars
])

if __name__ == '__main__':
    app.run_server(debug=True)
