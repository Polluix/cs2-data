import pandas as pd
from dash import Dash, html, dash_table, dcc, Input, Output,callback
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np

external_stylesheets = [dbc.themes.BOOTSTRAP]

mapApp = Dash(__name__,external_stylesheets=external_stylesheets)

#* map data dashboard
df = pd.read_csv("../src/maps_statistics.csv")
df = df.replace(',','', regex=True)

df_other = df.copy()

df_other.loc[pd.to_numeric(df_other["Matches"]) < 8e3, "Map"] = 'Other maps'
options = list(df_other["Map"].unique())

values = []
for row in df.iloc[8:10,4]:
    values.append(int(row))

soma = sum(values) #total number of matches

#removes 2 last rows of df_other
df_other.drop(df.tail(2).index, inplace=True)

#replaces data
other_dict = {
    'Map':'Other Maps',
    'Play Rate':'0',
    'T-Win %':'0',
    'CT-Win %':'0',
    'Matches':f'{soma}'
}

df_other = df_other._append(other_dict, ignore_index=True)

fig = px.pie(df_other, values="Matches", names="Map", title="Map Play Rate",
             color_discrete_sequence=px.colors.sequential.Blues)
fig.update_layout(paper_bgcolor='#092635', font_color="white")
options = list(df["Map"])

row = dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure=fig),
                    style={'backgroundColor':'#092635'}
                ),

                dbc.Col(
                    [
                        dcc.Dropdown(
                            options,
                            value=options[0],
                            id='maps',
                            clearable=False,
                        ),
            
                        dcc.Graph(
                            id = 'win-rate',
                            figure=fig,
                            style={'backgroundColor':'#092635'}
                        )
                    ]
                    
                )
            ],
            align="center",
            style={'backgroundColor':'#092635'}
        )

mapApp.layout = dbc.Container(
    row,
    fluid=True,
    style={'backgroundColor':'#092635'}
)


@mapApp.callback(
    Output('win-rate', 'figure'),
    Input('maps', 'value')
)
def update_output(value):
    if value == df.iloc[0,0]:
        val = [df.iloc[0,2].replace('%',''), df.iloc[0,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"], 
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[1,0]:
        val = [df.iloc[1,2].replace('%',''), df.iloc[1,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[2,0]:
        val = [df.iloc[2,2].replace('%',''), df.iloc[3,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[3,0]:
        val = [df.iloc[3,2].replace('%',''), df.iloc[3,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[4,0]:
        val = [df.iloc[4,2].replace('%',''), df.iloc[4,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[5,0]:
        val = [df.iloc[5,2].replace('%',''), df.iloc[5,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[6,0]:
        val = [df.iloc[6,2].replace('%',''), df.iloc[6,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[7,0]:
        val = [df.iloc[7,2].replace('%',''), df.iloc[7,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[8,0]:
        val = [df.iloc[8,2].replace('%',''), df.iloc[8,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    elif value == df.iloc[9,0]:
        val = [df.iloc[9,2].replace('%',''), df.iloc[9,3].replace('%','')]
        fig = px.pie(df, values=val, names=["T-Win %", "CT-Win %"],
                    title=f"{value} Win Rate", color_discrete_sequence=px.colors.sequential.Blues)
    
    fig.update_layout(paper_bgcolor='#092635', font_color="white")

    return fig

if __name__ == "__main__":
    mapApp.run_server(debug=True)