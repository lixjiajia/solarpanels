from dash import html, dcc
import dash_bootstrap_components as dbc
from charts import create_line_chart1, create_line_chart2, create_gauge_chart
import dash_leaflet as dl


# Home Layout
home_layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        # Header section
        html.Header(
            className="header",
            children=[
                html.Link(rel="stylesheet", href="solarpanels/assets/styles.css"),
                html.Div(
                    className="header-content",
                    children=[
                        html.Img(
                            src="assets/icons8-solar-64.png",
                            alt="Logo",
                            className="logo",
                        ),
                        html.H1("SolarOpt", className="title"),
                    ],
                ),
            ],
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
                        dl.Map(
                            dl.TileLayer(),
                            style={"height": "400px", "width": "100%"},
                            center=[51.0447, -114.0719],
                            zoom=6,
                        ),
                        # Form Section
                        html.Div(
                            className="form-section",
                            children=[
                                html.Form(
                                    action="/dashboard",
                                    method="get",
                                    children=[
                                        # Address and Roof Size input group
                                        html.Div(
                                            className="input-group",
                                            children=[
                                                html.Div(
                                                    className="input-item",
                                                    children=[
                                                        html.Label(
                                                            "Enter your Address"
                                                        ),
                                                        dcc.Input(
                                                            id="address",
                                                            name="address",
                                                            type="text",
                                                        ),
                                                    ],
                                                ),
                                                html.Div(
                                                    className="input-item",
                                                    children=[
                                                        html.Label(
                                                            "Enter your Roof Size (sqft)"
                                                        ),
                                                        dcc.Input(
                                                            id="roof-size",
                                                            name="roof-size",
                                                            type="number",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        # Energy Bills input
                                        html.Div(
                                            className="input-item",
                                            children=[
                                                html.Label(
                                                    "$ Cost of energy bills (per month)"
                                                ),
                                                dcc.Input(
                                                    id="energy-bills",
                                                    name="energy-bills",
                                                    type="number",
                                                ),
                                            ],
                                        ),
                                        # Home type or monthly consumption input
                                        html.Div(
                                            className="input-item",
                                            id="radio-input",
                                            children=[
                                                html.Label(
                                                    "Choose your home type or enter your average monthly consumption (kWh)"
                                                ),
                                                html.Div(
                                                    className="radio-input-items",
                                                    children=[
                                                        html.Div(
                                                            className="radio-group",
                                                            children=[
                                                                dcc.RadioItems(
                                                                    id="home-size",
                                                                    options=[
                                                                        {
                                                                            "label": "Small - 2000 sq.ft. and below",
                                                                            "value": "small",
                                                                        },
                                                                        {
                                                                            "label": "Medium - 2000 to 2600 sq.ft.",
                                                                            "value": "medium",
                                                                        },
                                                                        {
                                                                            "label": "Large - 2600 sq.ft. and above",
                                                                            "value": "large",
                                                                        },
                                                                    ],
                                                                    value="small",
                                                                )
                                                            ],
                                                        ),
                                                        html.Span(
                                                            "OR", className="or-text"
                                                        ),
                                                        dcc.Input(
                                                            id="monthly-consumption",
                                                            name="monthly-consumption",
                                                            type="number",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        # Submit Button
                                        html.Button(
                                            "Calculate",
                                            id="submit-btn",
                                            className="calculate-btn",
                                        ),
                                    ],
                                ),
                                # Display the result below the form
                                html.Div(id="result-output"),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Script(
            src="https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API_KEY}&libraries=places&callback=initMap",
            defer=True,
        ),
        # Load custom JavaScript
        html.Script(src="/assets/maps.js"),
    ],
)

dashboard_layout = html.Div(
    [
        html.H1(
            "SolarOpt",
            style={
                "marginBottom": "20px",
                "backgroundColor": "rgba(255,213,120,1.2)",
                "padding": "20px",
                "backgroundColor": "#f8f9fa",
                "borderRadius": "8px",
                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
            },
        ),
        dbc.Container(
            [
                # Row 1: Charts
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(
                                id="line_chart1",
                                figure=create_line_chart1(),
                                style={"boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
                            ),
                            width=6,
                        ),
                        dbc.Col(
                            dcc.Graph(
                                id="line_chart2",
                                figure=create_line_chart2(),
                                style={"boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
                            ),
                            width=6,
                        ),
                    ],
                    className="mb-4",
                ),
                # Row 2: Gauge Chart
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(
                                id="gauge_chart",
                                figure=create_gauge_chart(),
                                style={
                                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                                    "padding": "10px",
                                },
                            ),
                            width=6,
                            className="offset-md-3",
                        )
                    ],
                    className="mb-4",
                ),
            ],
            fluid=True,
        ),
    ]
)
