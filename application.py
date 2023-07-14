from dash import Dash, html, dcc, dash_table, Input, Output, State
import pandas as pd
import dash
import sys
from components import navbar, footer
import dash_bootstrap_components as dbc
sys.path.append('..')

# 1. Initialize the dash app
dash_app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP], 
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)

dash_app.title = "Portfolio Risk"
app = dash_app.server

# Define the pieces needed for the layout of the app
nav = navbar.Navbar()
footer = footer.Footer()


# Connect to your app pages
from pages import home, FINM350, FINM367

# Define the index page layout
dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        nav, 
        html.Div(id='page-content', children=[], className="container"),
        html.Br(),
        ],
        className="content" ),
    footer
    ],
    className='app-layout'
)

# Create the callback to handle mutlipage inputs
@dash_app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    if pathname == '/FINM367':
        return FINM367.layout
    if pathname == '/FINM350':
        return FINM350.layout
    else: # if redirected to unknown link
        return "404 Page Error! Please choose a link"

# Run the app on localhost:8050
if __name__ == '__main__':
    dash_app.run_server(debug=True)