from dash import Dash, dcc, html, Input, Output
from layouts import home_layout, dashboard_layout

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content", children=home_layout),
    ]
)


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname"), Input("submitButton", "n_clicks")],
)
def display_page(pathname, n_clicks):
    if pathname == "/dashboard" or (n_clicks and n_clicks > 0):
        return dashboard_layout
    return home_layout


if __name__ == "__main__":
    app.run_server(debug=True)
