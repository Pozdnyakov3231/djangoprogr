import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
from .models import Scooter

# Создаем Dash-приложение
app = DjangoDash("BatteryDashboard")

# Функция для получения данных из БД
def get_scooter_data():
    scooters = Scooter.objects.all()
    data = {
        "Модель": [scooter.model for scooter in scooters],
        "Уровень заряда": [scooter.battery_level for scooter in scooters]
    }
    return pd.DataFrame(data)

# Layout Dash-приложения (как в "Dash in 20 Minutes Tutorial")
app.layout = html.Div(children=[
    html.H1("Анализ уровня заряда самокатов"),
    
    dcc.Graph(id="battery-bar-chart"),  # Столбчатая диаграмма

    dcc.Interval(
        id="interval-update",
        interval=5000,  # Автообновление каждые 5 секунд
        n_intervals=0
    )
])

# Callback для обновления графика
@app.callback(
    dash.Output("battery-bar-chart", "figure"),
    dash.Input("interval-update", "n_intervals")
)
def update_graph(n_intervals):
    df = get_scooter_data()
    fig = px.bar(df, x="Модель", y="Уровень заряда",
                 title="Уровень заряда аккумуляторов",
                 labels={"value": "Процент", "variable": "Тип"})
    return fig
