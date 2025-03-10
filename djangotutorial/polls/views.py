from django.shortcuts import render
from django.http import HttpResponse
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
from .models import Scooter
from django.urls import path
from .views import battery_dash



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def battery_dash(request):
    return render(request, "polls/dash_template.html")