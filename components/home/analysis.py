from dash import html, Input, Output, State, callback
import requests

def Analysis():
    layout = html.Div(id="analysis-component",
                      style={'display': 'none'},
                      children = [html.H1("Analysis Component"),
                                  html.P(id="data-from-api")])
    return layout

@callback(
    Output('data-from-api', 'children'),
     Input('button-proceed', 'n_clicks'),
     State('portfolio-data', 'data'),
    prevent_initial_call=True
)
def getData(n_clicks, data):
    print(data)
    URL = 'https://api.portfolio-risk.com/info'
    response = requests.get(URL)
    return response.text