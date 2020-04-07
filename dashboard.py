import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
CS = 'https://codepen.io/chriddyp/pen/bWLwgP.css'

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FA, CS])
server = app.server
app.config['suppress_callback_exceptions'] = True

df = pd.read_csv('/home/aditi/Documents/IAT814/Project/BarCharts.csv')

# fig1 = go.Figure(data=[
#     go.Bar(name='Seniors Housing', x=df['Local Area'], y=df['Clientele - Seniors']),
#     go.Bar(name='Families and Others', x=df['Local Area'], y=df['NonSeniors'])
# ])
# fig1.update_layout(barmode='stack', title={
#     'text': "Distribution of Housing types in Vancouver",
#     'y': 0.9,
#     'x': 0.5,
#     'xanchor': 'center',
#     'yanchor': 'top'},
#                    xaxis_title="Local Area",
#                    yaxis_title="Percentage Housing",
#                    autosize=True,
#                    # width=1000,
#                    # height=500
#                    )
#
# fig2 = go.Figure(data=[
#     go.Bar(name='% Rented', x=df['Local Area'], y=df['Rented']),
#     go.Bar(name='% Owned', x=df['Local Area'], y=df['Owned'])
# ])
# fig2.update_layout(barmode='stack', title={
#     'text': "Distribution of Housing types in Vancouver",
#     'y': 0.9,
#     'x': 0.5,
#     'xanchor': 'center',
#     'yanchor': 'top'},
#                    xaxis_title="Local Area",
#                    yaxis_title="Percentage Housing",
#                    autosize=True,
#                    # width=1000,
#                    # height=500
#                    )

trace1 = go.Bar(name='% Seniors Housing', x=df['Local Area'], y=df['Clientele - Seniors'])
trace2 = go.Bar(name='% Families and Others', x=df['Local Area'], y=df['NonSeniors'])

trace3 = go.Bar(name='% Rented', x=df['Local Area'], y=df['Rented'])
trace4 = go.Bar(name='% Owned', x=df['Local Area'], y=df['Owned'])

fig1 = make_subplots(rows=2, cols=1,
                     shared_xaxes=True
                     )

fig1.append_trace(trace1, 1, 1)
fig1.append_trace(trace2, 1, 1)

fig1.append_trace(trace3, 2, 1)
fig1.append_trace(trace4, 2, 1)

fig1.update_layout(barmode='stack',
                   # legend_orientation="h",
                   # legend=dict(x=1.5, y=1.5),
                   title={
                       'text': "Distribution of Housing types in Vancouver",
                       'y': 0.9,
                       'x': 0.5,
                       'xanchor': 'center',
                       'yanchor': 'top',
                       # 'color':'#62B1F6'
                   },
                   # xaxis_title="Local Area",
                   # yaxis_title="Percentage value",
                   # autosize=True,
                   width=780,
                   height=700,
                   font=dict(
                       size=14,
                       # family="Courier New, monospace",
                       color="black"
                   )
                   )

trace1 = go.Bar(name='Current House Price', x=df['Local Area'], y=df['CURRENT_HOUSE_PRICE'])
trace2 = go.Bar(name='% Seniors', x=df['Local Area'], y=df['SeniorsPerFSApercentage'])

# trace3 = go.Bar(name='% Rented', x=df['Local Area'], y=df['Rented'])
# trace4 = go.Bar(name='% Owned', x=df['Local Area'], y=df['Owned'])

fig2 = make_subplots(rows=2, cols=1,
                     shared_xaxes=True
                     )

fig2.append_trace(trace1, 1, 1)
# fig.append_trace(trace2, 1, 1)
#
fig2.append_trace(trace2, 2, 1)
# fig.append_trace(trace4, 2, 1)
#
fig2.update_layout(title={
    'text': "Distribution of Housing prices and Seniors",
    'y': 0.9,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top',
    # 'color':'#62B1F6'
},
    # xaxis_title="Local Area",
    # yaxis_title="Percentage value",
    # autosize=True,
    width=780,
    height=700,
    font=dict(
        size=14,
        # family="Courier New, monospace",
        color="black"
    )
)

# fig3 = go.Figure(data=[
#     go.Bar(name='Current House Price', x=df['Local Area'], y=df['CURRENT_HOUSE_PRICE'])
# ])
# fig3.update_layout(title={
#     'text': "Distribution of Housing Prices in Vancouver",
#     'y': 0.9,
#     'x': 0.5,
#     'xanchor': 'center',
#     'yanchor': 'top'},
#     xaxis_title="Local Area",
#     yaxis_title="House Price",
#     autosize=False,
#     width=1000,
#     height=500,
# )
# fig4 = go.Figure(data=[
#     go.Bar(name='% Seniors', x=df['Local Area'], y=df['SeniorsPerFSApercentage'])
# ])
# fig4.update_layout(title={
#     'text': "Seniors in Vancouver",
#     'y': 0.9,
#     'x': 0.5,
#     'xanchor': 'center',
#     'yanchor': 'top'},
#     xaxis_title="Local Area",
#     yaxis_title="Percentage Seniors",
#     autosize=False,
#     width=1000,
#     height=500)

# map1 = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 html.Div
#                     (
#                     [
#                         html.H4("Non-market housing supply")
#                     ], className="offset-by-four column"
#                 )
#             ]
#         ),
#         dbc.Row(
#             [
#                 dbc.Row(
#                     html.Div(
#                         [
#
#                             html.Div(id="mapoutput")
#
#                         ]
#                     ), style={"height": "98%", "display": "inline-block", "position": "relative"},
#                     className="offset-by-one column nine columns"
#                 ),
#
#                 html.Div(
#                     daq.Slider(
#                         id='year',
#                         # vertical=True,
#                         min=1970,
#                         max=2019,
#                         size=500,
#                         value=2010,
#                         handleLabel={"showCurrentValue": True, "label": "Year"},
#                         marks={str(year): str(year) for year in (1970, 1980, 1990, 2000, 2010, 2019)},
#                         step=None
#                     ), style={"height": "2%", "display": "inline-block", "position": "relative"}
#                 )
#             ],
#
#         ),
#
#     ]
# )

map2 = dbc.Container(
    [
        dbc.Row(
            [
                html.Div
                    (
                    [
                        html.H5("Non-market housing supply", style={
                            'color': 'black'
                        })
                    ],
                    # className="offset-by-four column"
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(
                    [
                        dbc.Row(
                            html.Div(
                                [

                                    html.Div(id="mapoutput")

                                ]
                            ), style={"width": "98%", "display": "inline-block", "position": "relative"},
                            # className="offset-by-one column nine columns"
                        ),
                        dbc.Row(
                            html.Div(
                                daq.Slider(
                                    id='year',
                                    # vertical=True,
                                    min=1970,
                                    max=2019,
                                    size=450,
                                    value=2010,
                                    handleLabel={"showCurrentValue": True, "label": "Year"},
                                    marks={str(year): str(year) for year in (1970, 1980, 1990, 2000, 2010, 2019)},
                                    step=None
                                ), style={"width": "2%", "display": "inline-block", "position": "relative",
                                          "margin-left": "-3px"}
                                ,  # className="offset-by-one column one columns"
                            )
                        )

                    ]
                ), style={"width": "60%", "display": "inline-block", "position": "relative"},
                    # className="offset-by-one column nine columns"
                ),

                dbc.Col(html.Div(
                    [
                        dbc.Row(
                            html.Div(
                                [
                                    dcc.Graph(figure=fig1)

                                ]
                            ), style={"height": "50%", "display": "inline-block", "position": "relative"},
                            # className="offset-by-one column five columns"
                        ),

                        # dbc.Row(
                        #     html.Div(
                        #         [
                        #             # dcc.Graph(figure=fig2)
                        #
                        #         ]
                        #     ),
                        #     style={"height": "50%", "display": "inline-block", "position": "relative"},
                        #     # className="offset-by-one column nine columns"
                        # ),
                    ]
                ), style={"width": "40%", "display": "inline-block", "position": "relative"},
                    # className="offset-by-one column five columns"
                )
            ],

        ),

    ]
)


choro = dbc.Container(
    [
        dbc.Row(
            [
                html.Div
                    (
                    [
                        html.H5("Housing price", style={
                            'color': 'black'
                        })
                    ],
                    # className="offset-by-four column"
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(
                    [
                        dbc.Row(
                            html.Div(
                                [

                                    html.Div(
                                        html.Iframe(id='map',
                                                    srcDoc=open('/home/aditi/Documents/IAT814/Project/houseprice.html', 'r').read(),
                                                    width='100%', height='500'))

                                ]
                            ), style={"width": "98%", "display": "inline-block", "position": "relative"},
                            # className="offset-by-one column nine columns"
                        ),
                        dbc.Row(
                            # html.Div(
                            #     daq.Slider(
                            #         id='year',
                            #         # vertical=True,
                            #         min=1970,
                            #         max=2019,
                            #         size=450,
                            #         value=2010,
                            #         handleLabel={"showCurrentValue": True, "label": "Year"},
                            #         marks={str(year): str(year) for year in (1970, 1980, 1990, 2000, 2010, 2019)},
                            #         step=None
                            #     ), style={"width": "2%", "display": "inline-block", "position": "relative",
                            #               "margin-left": "-3px"}
                            #     ,  # className="offset-by-one column one columns"
                            # )
                        )

                    ]
                ), style={"width": "60%", "display": "inline-block", "position": "relative"},
                    # className="offset-by-one column nine columns"
                ),

                dbc.Col(html.Div(
                    [
                        dbc.Row(
                            html.Div(
                                [
                                    dcc.Graph(figure=fig2)

                                ]
                            ), style={"height": "50%", "display": "inline-block", "position": "relative"},
                            # className="offset-by-one column five columns"
                        ),

                        # dbc.Row(
                        #     html.Div(
                        #         [
                        #             # dcc.Graph(figure=fig2)
                        #
                        #         ]
                        #     ),
                        #     style={"height": "50%", "display": "inline-block", "position": "relative"},
                        #     # className="offset-by-one column nine columns"
                        # ),
                    ]
                ), style={"width": "40%", "display": "inline-block", "position": "relative"},
                    # className="offset-by-one column five columns"
                )
            ],

        ),

    ]
)

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


@app.callback(
    Output('mapoutput', 'children'),
    [Input('year', 'value')])
def update_figure(year):
    if year == 1970:
        return html.Iframe(id='map',
                           srcDoc=open('/home/aditi/Documents/IAT814/Project/map_1.html', 'r').read(),
                           width='100%', height='500')
    elif year == 1980:
        return html.Iframe(id='map',
                           srcDoc=open('/home/aditi/Documents/IAT814/Project/map_2.html', 'r').read(),
                           width='100%', height='500')
    elif year == 1990:
        return html.Iframe(id='map',
                           srcDoc=open('/home/aditi/Documents/IAT814/Project/map_3.html', 'r').read(),
                           width='100%', height='500')
    elif year == 2000:
        return html.Iframe(id='map',
                           srcDoc=open('/home/aditi/Documents/IAT814/Project/map_4.html', 'r').read(),
                           width='100%', height='500')
    elif year == 2010:
        return html.Iframe(id='map',
                           srcDoc=open('/home/aditi/Documents/IAT814/Project/map_5.html', 'r').read(),
                           width='100%', height='500')
    else:
        return html.Iframe(id='map',
                           srcDoc=open('/home/aditi/Documents/IAT814/Project/map_6.html', 'r').read(),
                           width='100%', height='500')


app.layout = html.Div([
    navbar,
    map2,
    choro
    # dcc.Graph(figure=fig3),
    # dcc.Graph(figure=fig2)
])

if __name__ == '__main__':
    app.run_server(debug=True)
