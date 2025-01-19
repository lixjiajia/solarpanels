from dash import Dash, dcc, html, Input, Output
from layouts import home_layout, dashboard_layout
import dash_leaflet as dl
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
    ],
)
server = app.server


app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content", children=home_layout),
    ]
)


@app.callback(
    Output("result-output", "children"),
    [Input("url", "pathname"), Input("submit-btn", "n_clicks")],
    [
        Input("address", "value"),
        Input("roof-size", "value"),
        Input("energy-bills", "value"),
        Input("home-size", "value"),
        Input("monthly-consumption", "value"),
    ],
)
def update_output(
    pathname, n_clicks, address, roof_size, energy_bills, home_size, monthly_consumption
):
    # if n_clicks is None:
    #     return ''

    if pathname == "/dashboard" or (n_clicks and n_clicks > 0):
        return dashboard_layout
    return home_layout


if __name__ == "__main__":
    app.run_server(debug=True)
