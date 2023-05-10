from django.urls import path
from . import views


urlpatterns = [
    path('', views.pu_result, name="pu-result"),
    path("summon-result/", views.summon_result, name="summon-result"),
]