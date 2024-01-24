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

player_df = pd.read_csv('../src/top_100_players.csv')
player_df.drop("Name", axis='columns', inplace=True)
player_df = player_df.replace(',','', regex=True)

regions = player_df['Region'].unique()

region_count = px.histogram(player_df, x='Region', title='Number of players per region',
                            color_discrete_sequence=px.colors.sequential.Blues, color='Region')

region_count.update_layout(
    {
        'plot_bgcolor':'rgba(0,0,0,0)',
        'paper_bgcolor':'rgba(0,0,0,0)',
        'font_color':'white',
    },
    title={
        'xanchor':'left',
    },
    showlegend=False
)


skill = px.scatter(player_df, x='Rank', y='CS Rating')

skill.update_yaxes(autorange='reversed')

skill.update_layout(
    {
        'plot_bgcolor':'rgba(0,0,0,0)',
        'paper_bgcolor':'rgba(0,0,0,0)',
        'font_color':'white',
    },
    yaxis = dict(
        tickmode='auto',
        nticks=6
    ),
    title='Skill rating per rank',
)

#2 rows and 2 collumns layout
row1 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(figure=region_count, style={'height':'50vh'}),
        ),

        dbc.Col(
            dcc.Graph(figure=skill, style={'height':'50vh'})
        )
    ]
)

row2 = dbc.Row(
    [
        dbc.Col(
           
        ),
        dbc.Col(
            
        )
    ]
)

playerApp.layout = dbc.Container(
    children=[
        row1,
        row2,
    ],
    fluid=True,
    style={
        'backgroundColor':'#092635',
        'height':'100vh',
        'width':'100vw'
    }
)

if __name__=='__main__':
    playerApp.run_server(debug=True)
