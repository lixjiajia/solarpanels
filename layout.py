from dash import html, dcc
from charts import create_line_chart, create_bar_chart, create_gauge_chart

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
    children=[
        html.H1("Dashboard", style={"textAlign": "center", "marginBottom": "20px"}),
        dcc.Graph(id="line_chart", figure=create_line_chart()),
        dcc.Graph(id="bar_chart", figure=create_bar_chart()),
        dcc.Graph(id="gauge_chart", figure=create_gauge_chart()),
    ]
)
