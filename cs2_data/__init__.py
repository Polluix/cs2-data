from dash import Dash, html, dash_table, dcc, Input, Output,callback
import dash_bootstrap_components as dbc

html.Div(
        html.H1(
            children="Counter Strike 2 Maps Analysis",
            id="page-title",
            style={
                'text-align':'center',
                'color':'white',
                'font-family':'arial',
                'font-size':34
            }
        )
    ),

html.Div(
        [
            'Author: ',
            html.A(
                children='Luiz Felipe Camargo Souza',
                href='https://www.linkedin.com/in/luiz-souza-b0706a23a/',
                target='_blank'
            ),
        ],
        style={
            'color':'white',
            'font-size':14
        }
    ),

html.Div(
        [
            'Access source code by clicking  ',
            html.A(
                children='here',
                href='https://github.com/Polluix/cs2-data',
                target='_blank'
            ),
        ],
        style={
            'color':'white',
            'font-size':14
        }
    ),
