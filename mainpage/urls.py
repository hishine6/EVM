from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('map/',views.map_status,name='map_status'),
]