from django.contrib import admin
from django.urls import include, path

from . import views
from .views import battery_chart

urlpatterns = [
    path("", views.index, name="index"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("battery_chart/", battery_chart, name="battery_chart")
]