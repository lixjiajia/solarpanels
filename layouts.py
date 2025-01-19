from dash import html, dcc
import dash_bootstrap_components as dbc
from charts import create_line_chart1, create_line_chart2, create_gauge_chart
import dash_leaflet as dl


# Home Layout
# Home Layout
home_layout = html.Div(
    children=[
        # Header Section
        html.Header(
            className="header",
            children=[
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
        # Main Content Section
        html.Main(
            className="main-content",
            children=[
                html.H1("POWERED TO HELP YOU OPT FOR THE CLEAN, SMART CHOICES."),
                html.Div(
                    className="content-container",
                    children=[
                        # Map Section
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
                                        # Input Group: Address and Roof Size
                                        html.Div(
                                            className="input-group",
                                            children=[
                                                html.Div(
                                                    className="input-item",
                                                    children=[
                                                        html.Label("Enter your Address"),
                                                        dcc.Input(
                                                            id="address",
                                                            name="address",
                                                            type="text",
                                                            placeholder="e.g., 123 Main St",
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
                                                            placeholder="e.g., 2000",
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        # Input Group: Energy Bills
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
                                                    placeholder="e.g., 150",
                                                ),
                                            ],
                                        ),
                                        # Input Group: Home Type or Monthly Consumption
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
                                                            placeholder="e.g., 800",
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
                                # Result Output Section
                                html.Div(id="result-output"),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)

dashboard_layout = html.Div(
    [
        # Header Section
        html.Header(
            className="header",
            children=[
                html.Div(
                    className="header-content",
                    children=[
                        html.Img(
                            src="assets/icons8-solar-64.png",
                            alt="Logo",
                            className="logo",
                        ),
                        html.H1("SolarOpt Dashboard", className="title"),
                    ],
                ),
            ],
        ),
        # Main Content Section
        html.Main(
            className="main-content",
            children=[
                html.Div(
                    className="content-container",
                    children=[
                        # Row 1: Line Charts
                        html.Div(
                            className="input-group",
                            children=[
                                dcc.Graph(
                                    id="line_chart1", figure=create_line_chart1()
                                ),
                                dcc.Graph(
                                    id="line_chart2", figure=create_line_chart2()
                                ),
                            ],
                        ),
                        # Row 2: Gauge Chart
                        html.Div(
                            className="input-item",
                            children=[
                                dcc.Graph(id="gauge_chart", figure=create_gauge_chart()),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ]
)
