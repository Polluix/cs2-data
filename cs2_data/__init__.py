import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dash import Dash, html, dash_table, dcc, Input, Output,callback
import plotly.express as px

app = Dash(__name__)

#* map data analysis
map_data = pd.read_csv("../src/maps_statistics.csv")
map_data = map_data.replace(',','', regex=True)
map_data.loc[pd.to_numeric(map_data["Matches"]) < 8e3, "Map"] = 'Other maps'
options = list(map_data["Map"])

fig = px.pie(map_data, values="Matches", names="Map", title="Map Play Rate")

app.layout = html.Div([
    html.Div(children='Dataset'),
    
    dash_table.DataTable(data=map_data.to_dict('records'), page_size=10),
    
    dcc.Graph(figure=fig),
    
    dcc.Dropdown(options, value=options[0], id='maps'),
    
    dcc.Graph(
        id = 'win-rate',
        figure=fig
    )
])

@app.callback(
    Output('win-rate', 'figure'),
    Input('maps', 'value')
)
def update_output(value):
    if value == map_data.iloc[0,0]:
        val = [map_data.iloc[0,2].replace('%',''), map_data.iloc[0,3].replace('%','')]
        fig = px.pie(map_data, values=val, names=["T-Win %", "CT-Win %"], title=f"{value} Win Rate")
    return fig

if __name__ == "__main__":
    app.run(debug=True)