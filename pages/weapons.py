import pandas as pd
from dash import Dash, html, dash_table, dcc, Input, Output,callback
import dash_bootstrap_components as dbc
import plotly.express as px

weapon_df = pd.read_csv('../src/weapons_statistics.csv')

external_stylesheets = [dbc.themes.BOOTSTRAP]

weaponApp = Dash(__name__,external_stylesheets=external_stylesheets)

#* pizza com lugar de acerto
#* pizza total kills
#* kills per round

options = weapon_df['Weapon']
options = [str(i) for i in options]

kpr = px.bar(weapon_df,x='Weapon', y='KPR', color='Weapon',
             color_discrete_sequence=px.colors.sequential.Blues, text_auto=True,
             title='Weapon KPR')

kpr.update_layout(
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
    ),
    title={
        'x':0.5,
        'y':0.9,
        'xanchor':'center',
        'yanchor':'top'
    },
    margin={
        't':50
    }
    
)

kpr.update_traces(
    textposition='outside'
)

row1 = dbc.Row(
    [
        dbc.Col(dcc.Graph()),
        dbc.Col(dcc.Graph())
    ]
)

row2 = dbc.Row(
    dcc.Graph(figure=kpr)
)

weaponApp.layout = dbc.Container(
    children=[
        row1,
        row2
    ],
    fluid=True,
    style={
        'backgroundColor':'#092635',
        'height':'150vh',
        'width':'100vw'
    }
)

if __name__=='__main__':
    weaponApp.run_server(debug=True)
