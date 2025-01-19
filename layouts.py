from dash import html, dcc
import dash_bootstrap_components as dbc
from charts import create_line_chart1, create_line_chart2, create_gauge_chart

# Home Layout
home_layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f4f4f4",
        "color": "#333",
        "margin": "0",
        "padding": "0",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "100vh",
    },
    children=[
        html.Div(
            style={
                "backgroundColor": "#fff",
                "padding": "20px",
                "borderRadius": "8px",
                "boxShadow": "0 0 10px rgba(0, 0, 0, 0.1)",
                "maxWidth": "500px",
                "width": "100%",
            },
            children=[
                html.H1(
                    "Welcome to Solar Sisters",
                    style={
                        "fontSize": "24px",
                        "marginBottom": "20px",
                        "color": "#007bff",
                        "textAlign": "center",
                    },
                ),
                html.Div(
                    style={"display": "flex", "flexDirection": "column", "gap": "15px"},
                    children=[
                        html.Label("Roof size:"),
                        dcc.Input(
                            type="text",
                            id="roofSize",
                            required=True,
                            style={"width": "100%", "padding": "10px"},
                        ),
                        html.Label("Consumption of kW per month:"),
                        dcc.Input(
                            type="text",
                            id="ConsumptionMonth",
                            required=True,
                            style={"width": "100%", "padding": "10px"},
                        ),
                        html.Label("Cost of energy bills per month:"),
                        dcc.Input(
                            type="text",
                            id="EnergyBillMonth",
                            required=True,
                            style={"width": "100%", "padding": "10px"},
                        ),
                        html.Button(
                            "Submit",
                            id="submitButton",
                            n_clicks=0,
                            style={
                                "width": "100%",
                                "padding": "10px",
                                "marginTop": "15px",
                                "borderRadius": "4px",
                                "backgroundColor": "#007bff",
                                "color": "white",
                                "fontSize": "16px",
                                "cursor": "pointer",
                            },
                        ),
                    ],
                ),
            ],
        )
    ],
)

dashboard_layout = html.Div(
    [
        html.H1(
            "SOLAROPT",
            style={
                "marginBottom": "20px",
                "backgroundColor": "rgba(255,213,120,1.2)",
                "padding": "20px",
                "borderRadius": "8px",
                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
            },
        ),
        html.Div(
            [
                html.H2(
                    "Emissions Savings",
                    style={"textAlign": "center", "marginBottom": "20px"},
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(
                                        id="line_chart",
                                        figure=create_line_chart1(),
                                        style={
                                            "width": "80%",
                                            "textAlign": "center",
                                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                                            "padding": "10px",
                                        },
                                    ),
                                    width=7,
                                ),
                                dbc.Col(
                                    html.Div(
                                        children=[
                                            html.H3(
                                                "1 year CO2 savings",
                                                style={
                                                    "fontSize": "24px",
                                                    "textAlign": "center",
                                                },
                                            ),
                                            html.H2(
                                                "X lbs",
                                                style={
                                                    "fontSize": "32px",
                                                    "fontWeight": "bold",
                                                    "textAlign": "center",
                                                },
                                            ),
                                        ],
                                        style={
                                            "border": "2px solid #4CAF50",
                                            "borderRadius": "10px",
                                            "padding": "20px",
                                            "textAlign": "center",
                                            "boxShadow": "4px 8px 12px rgba(0, 0, 0, 0.1)",
                                            "backgroundColor": "rgba(255,213,120,0.8)",
                                            "margin": "0 auto",
                                        },
                                    ),
                                    width=5,
                                ),
                            ],
                            justify="center",
                            align="center",
                            style={"marginBottom": "20px"},
                        ),
                    ]
                ),
            ]
        ),
    ]
)
