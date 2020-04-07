import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def map():
    df = pd.read_csv('/home/aditi/Documents/IAT814/Project/BarCharts.csv')

    trace1 = go.Bar(name='Current House Price', x=df['Local Area'], y=df['CURRENT_HOUSE_PRICE'])
    trace2 = go.Bar(name='% Seniors', x=df['Local Area'], y=df['SeniorsPerFSApercentage'])

    # trace3 = go.Bar(name='% Rented', x=df['Local Area'], y=df['Rented'])
    # trace4 = go.Bar(name='% Owned', x=df['Local Area'], y=df['Owned'])

    fig = make_subplots(rows=2, cols=1,
                        shared_xaxes=True
                        )

    fig.append_trace(trace1, 1, 1)
    # fig.append_trace(trace2, 1, 1)
    #
    fig.append_trace(trace2, 2, 1)
    # fig.append_trace(trace4, 2, 1)
    #
    fig.update_layout(
                      # legend_orientation="h",
                      # legend=dict(x=1.5, y=1.5),
                      title={
        'text': "Distribution of Housing prices and Seniors",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
                       # xaxis_title="Local Area",
                       yaxis_title="House Price",
                       autosize=True,
                       # width=1000,
                       # height=500
                       )
    fig.show()


if __name__ == '__main__':
    map()
