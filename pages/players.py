import pandas as pd
from dash import Dash, html, dash_table, dcc, Input, Output,callback
import dash_bootstrap_components as dbc
import plotly.express as px

external_stylesheets = [dbc.themes.BOOTSTRAP]

playerApp = Dash(__name__,external_stylesheets=external_stylesheets)

#* concentração por regiao
#* skill rating 
#* win rate

player_df = pd.read_csv('../src/top_100_players.csv')
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

p_df = pd.DataFrame({
    'Name': player_df.iloc[0,1],
    'result':['Wins', 'Losses', 'Tie'],
    'count':[player_df.iloc[0,6], player_df.iloc[0,5], player_df.iloc[0,4]]
})

wl = px.bar(p_df, x='result', y='count', color='result',
            color_discrete_sequence=px.colors.sequential.Blues,
            text_auto=True)

wl.update_layout(
    {
        'plot_bgcolor':'rgba(0,0,0,0)',
        'paper_bgcolor':'rgba(0,0,0,0)',
        'font_color':'white',
    },
    showlegend=False,
    yaxis = dict(
            showticklabels=False,
            showgrid=False,
            visible=False
    )
)
wl.update_traces(textposition='outside')

player_names = player_df['Name']
player_names = [str(i) for i in player_names] #options for win/loss graph

dropdown_players = dcc.Dropdown(
    id='drop-players',
    clearable=False,
    options = player_names,
    value=player_names[0]
)

#2 rows and 2 collumns layout
row1 = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(figure=region_count),
        ),
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            'Player W/L. Select player:',
                            style={
                                'color':'white'
                            } 
                        ),
                        dropdown_players,   
                    ]
                ),
                
                dcc.Graph(
                    figure=wl,
                    id='wl-graph'
                )
            ]
           
        )
    ]
)

row2 = dbc.Row(
    dbc.Col(
        dcc.Graph(figure=skill)
    )
)

playerApp.layout = dbc.Container(
    children=[
        row1,
        row2,
    ],
    fluid=True,
    style={
        'backgroundColor':'#092635',
        'height':'150vh',
        'width':'100vw'
    }
)

@playerApp.callback(
    Output('wl-graph','figure'),
    Input('drop-players', 'value')   
)
def update_output(value):
    index = player_df.index[player_df['Name']==value].values
    print(player_df.loc[index, 'Wins'])
    p_df = pd.DataFrame({
        'Name': value,
        'result':['Ties', 'Losses', 'Wins'],
        'count':[
            str(player_df.loc[index, 'Ties'].values[0]),
            str(player_df.loc[index, 'Losses'].values[0]),
            str(player_df.loc[index, 'Wins'].values[0]),
        ]
    })
    # print(p_df)
    wl = px.bar(p_df, x='result', y='count', color='result',
            color_discrete_sequence=px.colors.sequential.Blues,
            text_auto=True)

    wl.update_layout(
        {
            'plot_bgcolor':'rgba(0,0,0,0)',
            'paper_bgcolor':'rgba(0,0,0,0)',
            'font_color':'white',
        },
        showlegend=False,
        yaxis = dict(
            showticklabels=False,
            showgrid=False,
            visible=False
        )
    )
    
    wl.update_traces(textposition='outside')

    return wl



if __name__=='__main__':
    playerApp.run_server(debug=True)
