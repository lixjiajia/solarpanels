import plotly.graph_objects as go
import plotly.express as px
import numpy as np

month = np.arange(1, 13)

# Random Data kWh from energy per month
solar_energy = np.random.uniform(500, 1000, 12)
gas_energy = np.random.uniform(800, 1200, 12)

solar_cost = solar_energy * 0.1
gas_cost = gas_energy * 0.15

# Random Data kg CO2 per kWh
solar_emissions = solar_energy * 0.02
gas_emissions = gas_energy * 0.6

yearly_gas_cost = np.sum(gas_cost)
yearly_solar_cost = np.sum(solar_cost)


def create_line_chart1():
    fig = px.line(
        x=month,
        y=[solar_cost, gas_cost],
        labels={"x": "Month", "y": "Cost ($)"},
        title="Monthly Energy Cost (Solar vs Gas)",
    )
    fig.data[0].name = "Solar Cost"
    fig.data[1].name = "Gas Cost"
    return fig


def create_line_chart2():
    fig = px.line(
        x=month,
        y=[solar_emissions, gas_emissions],
        labels={"x": "Month", "y": "CO2 Emissions (kg)"},
        title="Monthly CO2 Emissions (Solar vs Gas)",
    )
    fig.data[0].name = "Solar Emissions"
    fig.data[1].name = "Gas Emissions"
    return fig


def create_gauge_chart():
    savings_percentage = (yearly_gas_cost - yearly_solar_cost) / yearly_gas_cost * 100
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=savings_percentage,
            title={"text": "Yearly Energy Cost Savings"},
            number={"suffix": "%", "font": {"size": 36, "color": "blue"}},
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickformat": ".0f",
                    "ticksuffix": "%",
                    "tickcolor": "black",
                },
                "bar": {"color": "blue", "thickness": 0.3},
                "steps": [
                    {"range": [0, savings_percentage], "color": "pink"},
                    {"range": [savings_percentage, 100], "color": "lightgray"},
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": savings_percentage,
                },
            },
        )
    )
    return fig
