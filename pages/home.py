import dash
import base64
import io
from dash import html, dcc, dash_table, Input, Output, callback
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, path='/'),

layout = html.Div(
    children=[
        html.Br(),
        html.H1(children='Welcome to Portfolio and Risk Management!!'),

        html.Div(children='''
            This is our Home page content, where hopefully we will have some explanation and links for what this site is. 
            If you would like to do analysis on a custom portfolio, upload an Excel or csv below containing the relevant tickers and quantities.
            Otherwise, feel free to begin your analysis with the default portfolio displayed in the table.
        '''),
        html.Br(),
        dbc.Row([
            dbc.Col(
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        DashIconify(icon="material-symbols:upload-sharp", width=30, className="margin-right-10"),
                        html.Div("Drag and Drop or ", style={'white-space': 'pre'}), 
                        html.A('Select File', className='bold-anchor')
                        ],
                        style={'display': 'flex',
                                'align-items': 'center',
                                'justify-content': 'center'}),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    # Allow multiple files to be uploaded
                    multiple=False
                )),
            dbc.Col(
                dbc.Button("Continue with Default", id="button-use-default", color="primary"),
                width="auto"
            )],
            align="center"
        ),
        html.Div(id='output-data-upload'),
    ],
        
)

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        )
    ])

@callback(Output('output-data-upload', 'children', allow_duplicate=True),
            [Input('upload-data', 'contents'),
               Input('upload-data', 'filename')],
            prevent_initial_call=True)
def update_output(contents, filename):
    if contents is not None:
        children = [parse_contents(contents, filename)]
        return children
    
@callback(
    Output('output-data-upload', 'children'),
    Input('button-use-default', 'n_clicks'),
    prevent_initial_call=True)
def update_output_to_default(n_clicks):
    portfolio_data = pd.read_excel("./data/holdings_example_2023_05_14_nocash.xlsx", sheet_name="Sheet1")
    return dash_table.DataTable(portfolio_data.to_dict('records'))