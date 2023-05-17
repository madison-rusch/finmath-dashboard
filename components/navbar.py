# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc
import dash

def Navbar():
    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/")),
                dbc.NavItem(dbc.NavLink("FINM 350", href="/FINM350")),
                dbc.NavItem(dbc.NavLink("FINM 367", href="/FINM367")),
            ] ,
            brand=[
                dbc.Row([
                        dbc.Col(html.Img(src=dash.get_asset_url('shield_logo.svg'), height="30px")),
                        dbc.Col(dbc.NavbarBrand("FinMath Portfolio Dashboards", className="ms-2")),])
                    ],
            brand_href="/",
            color="dark",
            dark=True,
            
        ), 
    ])

    return layout