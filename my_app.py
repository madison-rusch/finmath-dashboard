from dash import Dash, html, dcc, dash_table, Input, Output, State
import pandas as pd
import dash
import sys
from components import navbar
import dash_bootstrap_components as dbc
sys.path.append('..')

# Github Auth token: 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
# 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

dash_app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP], 
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)

dash_app.title = "Portfolio Risk"
app = dash_app.server

# Define the navbar
nav = navbar.Navbar()

# Connect to your app pages
from pages import home, FINM350, FINM367

# Define the index page layout
dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
    dcc.Store(id='home-layout', data=[home.layout]),
    dcc.Store(id='FINM350-layout', data=[FINM350.layout]),
    dcc.Store(id='FINM367-layout', data=[FINM367.layout]),
])



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
    
# app.clientside_callback(
#     """
#     function(pathname, home, FINM367, FINM350) {
#         if (pathname == '/') {
#             return home;
#         }
#         if (pathname == '/FINM367') {
#             return FINM367;
#         }
#         if (pathname == '/FINM350') {
#             return FINM350;
#         }
#         else { 
#             return "404 Page Error! Please choose a link";
#         }
#     }
#     """,
#     Output('page-content', 'children'),
#     Input('url', 'pathname'),
#     State('home-layout', 'data'),
#     State('FINM367-layout', 'data'),
#     State('FINM350-layout', 'data'),
# )

# Run the app on localhost:8050
if __name__ == '__main__':
    dash_app.run_server(debug=True)