import pandas as pd
from dash import Dash, html, dash_table, dcc, Input, Output,callback
import dash_bootstrap_components as dbc
import plotly.express as px

df = pd.read_csv('../src/top_100_players.csv')

external_stylesheets = [dbc.themes.BOOTSTRAP]

playerApp = Dash(__name__,external_stylesheets=external_stylesheets)

#* concentração por regiao
#* skill rating 
#* win rate
#* win/loss por jogador

row1 = dbc.Row(
    [
        dbc.Col(),
        dbc.COl()
    ]
)

row2 = dbc.Row(
    [
        dbc.Col(),
        dbc.COl()
    ]
)

playerApp.layout = dbc.Container(
    row,
    fluid=True,
    style={'backgroundColor':'#092635'}
)

if __name__=='__main__':
    playerApp.run_server(debug=True)
