from dash import Dash, dcc, html, page_container, callback, Input, Output, page_registry
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = Dash(__name__,external_stylesheets=external_stylesheets, use_pages=True)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Maps", href="/maps")),
        dbc.NavItem(dbc.NavLink("Players", href="/players")),
        dbc.NavItem(dbc.NavLink("Weapons", href="/weapons"))
    ],
    brand="Counter Strike 2 Analysis",
    color="dark",
    dark=True,
    className="mb-2",
)

container = dbc.Container(id='page-container', fluid=True, className='mb-4')

app.layout = dbc.Container(
    [
        navbar,
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
        page_container
    ],
    fluid=True,
    style={
        'backgroundColor':'#092635',
    }
)    

if __name__=='__main__':
    app.run_server(debug=True)
