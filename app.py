from dash import Dash, dcc, html, Input, Output
from layouts import home_layout, dashboard_layout
import dash_leaflet as dl

app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=["https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"])
server = app.server

app.layout = html.Div(
    children=[
        # Header section
        html.Header(
            className="header",
            children=[
                html.Link(rel="stylesheet", href="assets/styles.css"),
                html.Div(
                    className="header-content",
                    children=[
                        html.Img(src="assets/icons8-solar-64.png", alt="Logo", className="logo"),
                        html.H1("SolarOpt", className="title")
                    ]
                )
            ]
        ),

        # Main content section
        html.Main(
            className="main-content",
            children=[
                html.H1("POWERED TO HELP YOU OPT FOR THE CLEAN, SMART CHOICES."),
                html.Div(
                    className="content-container",
                    children=[
                        # Set center to Calgary
                        dl.Map(dl.TileLayer(), style={'height': '400px', 'width': '100%'}, center=[51.0447, -114.0719], zoom=6),
                        # Form Section
                        html.Div(
                            className="form-section",
                            children=[
                                html.Form(
                                    action="/solar-visualizations",
                                    method="get",
                                    children=[
                                        # Address and Roof Size input group
                                        html.Div(
                                            className="input-group",
                                            children=[
                                                html.Div(
                                                    className="input-item",
                                                    children=[
                                                        html.Label("Enter your Address"),
                                                        dcc.Input(id="address", name="address", type="text")
                                                    ]
                                                ),
                                                html.Div(
                                                    className="input-item",
                                                    children=[
                                                        html.Label("Enter your Roof Size (sqft)"),
                                                        dcc.Input(id="roof-size", name="roof-size", type="number")
                                                    ]
                                                )
                                            ]
                                        ),
                                        # Energy Bills input
                                        html.Div(
                                            className="input-item",
                                            children=[
                                                html.Label("$ Cost of energy bills (per month)"),
                                                dcc.Input(id="energy-bills", name="energy-bills", type="number")
                                            ]
                                        ),
                                        # Home type or monthly consumption input
                                        html.Div(
                                            className="input-item", id="radio-input",
                                            children=[
                                                html.Label("Choose your home type or enter your average monthly consumption (kWh)"),
                                                html.Div(
                                                    className="radio-input-items",
                                                    children=[
                                                        html.Div(
                                                            className="radio-group",
                                                            children=[
                                                                dcc.RadioItems(
                                                                    id="home-size",
                                                                    options=[
                                                                        {'label': 'Small - 2000 sq.ft. and below', 'value': 'small'},
                                                                        {'label': 'Medium - 2000 to 2600 sq.ft.', 'value': 'medium'},
                                                                        {'label': 'Large - 2600 sq.ft. and above', 'value': 'large'}
                                                                    ],
                                                                    value='small'
                                                                )
                                                            ]
                                                        ),
                                                        html.Span("OR", className="or-text"),
                                                        dcc.Input(id="monthly-consumption", name="monthly-consumption", type="number")
                                                    ]
                                                )
                                            ]
                                        ),
                                        # Submit Button
                                        html.Button('Calculate', id='submit-btn', className="calculate-btn")
                                    ]
                                ),
                                # Display the result below the form
                                html.Div(id="result-output")
                            ]
                        )
                    ]
                )
            ]
        ),
    html.Script(
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDn0bGHSbh5yHc4o1fKAccYnkOsTdZ72Do&libraries=places&callback=initMap",
        defer=True,
    ),
    # Load custom JavaScript
    html.Script(src="/assets/maps.js"),
    ]
)




@app.callback(
    Output('result-output', 'children'),
    [Input('submit-btn', 'n_clicks')],
    [Input('address', 'value'),
     Input('roof-size', 'value'),
     Input('energy-bills', 'value'),
     Input('home-size', 'value'),
     Input('monthly-consumption', 'value')]
)
def update_output(n_clicks, address, roof_size, energy_bills, home_size, monthly_consumption):
    if n_clicks is None:
        return ''

    result = f"Address: {address}, Roof Size: {roof_size} sqft, Energy Bills: ${energy_bills}, Home Size: {home_size}, Monthly Consumption: {monthly_consumption} kWh"
    return f"Form Submitted! {result}"

def display_page(pathname, n_clicks):
    if pathname == "/dashboard" or (n_clicks and n_clicks > 0):
        return dashboard_layout
    return home_layout


if __name__ == "__main__":
    app.run_server(debug=True)
