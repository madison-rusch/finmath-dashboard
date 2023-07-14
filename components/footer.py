# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc
import dash

def Footer():
    layout = html.Div([
        html.Footer(children=[
            html.Div(
                children=[
                    html.Br(),
                    html.Div("© 2023 UChicago Financial Mathematics"),
                    html.Br()],
                className="container")
        ],
        className="app-footer")
    ])

    return layout