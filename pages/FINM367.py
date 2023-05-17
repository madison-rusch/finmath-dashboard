# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc


# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("FINM 367")),
        html.Br(),
        html.Hr(),
        dbc.Col([
            html.P("Filters"), 
            dbc.Button("Test Button", color="primary")
        ]), 
        dbc.Col([
            html.P("FinMath 367: Portfolio Theory and Management"), 
            html.P("You can add many cool components using the bootstrap dash components library."),
        ])
    ])
])