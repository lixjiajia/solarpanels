import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from dash import Dash
from dash import html
import dash
from dash import dash_table
from dash import dcc
from dash.dependencies import Input, Output

matplotlib.use("agg")

# from .layout import html_layout


def display_line_chart1(
    x, y_gas, y_solar, solar_legend_label, gas_legend_label, x_label, y_label, title
):
    plt.figure(figsize=(15, 10))
    print("plt figure")

    plt.plot(
        x,
        y_solar,
        label=solar_legend_label,
        marker="o",
        color="blue",
        linewidth=2,
        markersize=8,
    )
    plt.plot(
        x,
        y_gas,
        label=gas_legend_label,
        marker="s",
        color="red",
        linewidth=2,
        markersize=8,
    )

    plt.xlabel(x_label, fontsize=15, labelpad=20, weight="bold", loc="center")
    plt.ylabel(y_label, fontsize=15, labelpad=20, weight="bold", loc="center")
    plt.title(title, fontsize=30, pad=25, weight="bold", loc="center")
    plt.grid(which="both", linestyle="--", linewidth=0.5, alpha=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.legend(fontsize=10, loc="upper right", frameon=True, shadow=True, borderpad=1)
    plt.tight_layout()
    print("tight")
    return plt


def register_callbacks(app, line_chart1, line_chart2, gauge_chart):

    @app.callback(
        [
            Output("histogram-graph", "figure"),
            Output("gauge-chart", "figure"),
        ],
        [Input("url", "pathname")],
    )
    def init_visualizations(app, line_chart1, line_chart2, gauge_chart):
        """Create a Plotly Dash dashboard."""
        dash_app = dash.Dash(
            server=app,
            # routes_pathname_prefix="/dashapp/",
            # external_stylesheets=[
            #     "/static/dist/css/styles.css",
            # ],
        )

        # dash_app.index_string = html_layout
        print("plot2")
        print(line_chart1)

        dash_app.layout = html.Div(
            className="visualizations",
            children=[
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=line_chart1,
                            className="graph",
                            id="histogram-graph",
                        ),
                    ],
                    id="dash-container",
                )
            ],
        )
        return dash_app.server
