from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from layouts import home_layout, dashboard_layout
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@100..700&display=swap",
    ],
)


server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content"),
    ]
)

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")],
)
def display_page(pathname):
    if pathname == "/dashboard":
        return dashboard_layout
    return home_layout


if __name__ == "__main__":
    app.run_server(debug=True)
