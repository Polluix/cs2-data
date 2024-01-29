import pandas as pd
from dash import dcc, Input, Output,callback, register_page
import dash_bootstrap_components as dbc
import plotly.express as px

weapon_df = pd.read_csv('./src/weapons_statistics.csv')

weapon_df = weapon_df.replace('%', '', regex=True)
weapon_df = weapon_df.replace(',', '', regex=True)

external_stylesheets = [dbc.themes.BOOTSTRAP]

register_page(__name__, name='weapons', external_stylesheets = external_stylesheets)

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

hit_frame = pd.DataFrame({
    'count':[
        weapon_df.loc[0, 'HS %'],
        weapon_df.loc[0, 'Chest %'],
        weapon_df.loc[0, 'Leg %']
    ]},
    index =[
        'HS %', 
        'Chest %', 
        'Leg %', 
    ]
)

hit_drop = dcc.Dropdown(
    options=options,
    clearable=False,
    value=options[0],
    id='hit-drop'
)

hit = px.pie(hit_frame, values='count', names=[
        'HS %', 
        'Chest %', 
        'Leg %', 
    ], color_discrete_sequence= [
        px.colors.sequential.Blues[0],
        px.colors.sequential.Blues[4],
        px.colors.sequential.Blues[8]
    ],
    title = 'Hit %')

hit.update_layout(
    {
        'plot_bgcolor':'rgba(0,0,0,0)',
        'paper_bgcolor':'rgba(0,0,0,0)',
        'font_color':'white',
    },
    title={
        'x':0.5,
        'y':0.9,
        'xanchor':'center',
        'yanchor':'top'
    },
)

tk_df = pd.DataFrame(
    {
        'count':weapon_df['Total Kills'].to_list()
    }, index=weapon_df['Weapon'].to_list()
)

tk = px.pie(tk_df, values='count', title='Total Kills',
            names=weapon_df['Weapon'].to_list())

tk.update_layout(
    {
        'plot_bgcolor':'rgba(0,0,0,0)',
        'paper_bgcolor':'rgba(0,0,0,0)',
        'font_color':'white',
    },
    title={
        'x':0.5,
        'y':0.9,
        'xanchor':'center',
        'yanchor':'top'
    },
)

row1 = dbc.Row(
    [
        dbc.Col(
            [
                hit_drop,
                dcc.Graph(figure=hit, id='hit-fig')
            ]
        ),
        dbc.Col(
            [
                dcc.Graph(figure=tk, id='tk-fig')
            ]
        )
    ]
)

row2 = dbc.Row(
    dcc.Graph(figure=kpr)
)

def layout():
    layout = dbc.Container(
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

    return layout

@callback(
    Output('hit-fig', 'figure'),
    Input('hit-drop', 'value')
)
def update_output(value):
    index =weapon_df.isin([value]).any(axis=1).idxmax()
    hit_frame = pd.DataFrame({
        'count':[
            weapon_df.loc[index, 'HS %'],
            weapon_df.loc[index, 'Chest %'],
            weapon_df.loc[index, 'Leg %']
        ]},
        index =[
            'HS %', 
            'Chest %', 
            'Leg %', 
        ]
    )

    hit = px.pie(hit_frame, values='count', names=[
        'HS %', 
        'Chest %', 
        'Leg %', 
    ], color_discrete_sequence= [
        px.colors.sequential.Blues[0],
        px.colors.sequential.Blues[4],
        px.colors.sequential.Blues[8]
    ],
    title = 'Hit %')

    hit.update_layout(
        {
            'plot_bgcolor':'rgba(0,0,0,0)',
            'paper_bgcolor':'rgba(0,0,0,0)',
            'font_color':'white',
        },
        title={
            'x':0.5,
            'y':0.9,
            'xanchor':'center',
            'yanchor':'top'
        },
    )
    hit.update_traces(
        text = [value for value in hit_frame['count'] + '%'],
        textinfo='text'
    )

    return hit
