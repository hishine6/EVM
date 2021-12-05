from django.urls import path
from .views import *

app_name = 'app_connection'

urlpatterns = [
    path('get_all_station', get_all_station),
]