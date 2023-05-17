import dash
import os.path
from dash import html, dcc, dash_table
import pandas as pd

dash.register_page(__name__, path='/'),

portfolio_data = pd.read_excel("./data/holdings_example_2023_05_14_nocash.xlsx", sheet_name="Sheet1")

layout = html.Div(children=[
    html.H1(children='Welcome to FinMath!!'),

    html.Div(children='''
        This is our Home page content, where hopefully we will have some explanation and links for what this site is. Meanwhile, here's our portfolio objects
    '''),
    
    dash_table.DataTable(data=portfolio_data.to_dict('records'), 
                         page_size=30,
                         style_cell={"width": "auto"})
])