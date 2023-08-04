import dash
import base64
import io
from dash import html, dcc, dash_table, Input, Output, callback
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import pandas as pd

from components.home import loadData, analysis

dash.register_page(__name__, path='/'),

loadData = loadData.LoadData()
analysis = analysis.Analysis()

layout = html.Div(
    [
        loadData,
        analysis,
        html.Div(id='proceed', children=[
                dbc.Row([
                    dbc.Col(dbc.Button("Proceed to Analysis", id="button-proceed", color="primary", class_name="margin-top-10"),
                        width="auto"
                    )],
                    justify="end"
                )],
                style={'display': 'none'})
    ]
)

# Outputs: 
# output-data-upload: data table display of portfolio
# portfolio-data: dict of data stored in Store for rest of analysis
# proceed: display proceed button when data loaded
# Inputs:
# button-use-default: use default data stored in app
@callback(
    [Output('load-data-component', 'style'),
    Output('analysis-component', 'style')],
    Input('button-proceed', 'n_clicks'),
    prevent_initial_call=True)
def proceed_to_analysis(n_clicks):
    return {'display':'none'}, {'display': 'block'}