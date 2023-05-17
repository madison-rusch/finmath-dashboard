from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd
import dash
import sys
import dash_bootstrap_components as dbc
sys.path.append('..')
    
# # app = dash.Dash(
# #     external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
# # )

# # sidebar = html.Div(
# #     children = [
# #         html.H2("Filters"),
# #         html.Hr(),
# #         html.P(
# #             "A simple sidebar layout with filters", className="lead"
# #         ),
# #         dbc.Nav(
# #             [
# #                 dcc.Dropdown(id = 'one'),
# #                 html.Br(),
# #                 dcc.Dropdown(id = 'two'),
# #                 html.Br(),
# #                 dcc.Dropdown(id = 'three')

# #             ],
# #             vertical=True,
# #             pills=True,
# #         ),
# #     ]
# #     # style=SIDEBAR_STYLE,
# # )



# app.layout = html.Div(children = [
#     dbc.Row(navbar),
#     dbc.Row([
#             dbc.Col(sidebar),
#             dbc.Col()])
#     ]

    
    
#     # [
# 	# html.H1('FinMath Portfolio Dashboard'),

#     # html.Div(
#     #     [
#     #         html.Div(
#     #             dcc.Link(
#     #                 f"{page['name']} - {page['path']}", href=page["relative_path"]
#     #             )
#     #         )
#     #         for page in dash.page_registry.values()
#     #     ]
#     # ),

# 	# dash.page_container
# #  ]
# )

# if __name__ == '__main__':
# 	app.run_server(debug=True)


app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP], 
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)