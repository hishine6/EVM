from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('map/',views.map_status,name='map_status'),
    path('list_status/',views.list_status,name='list_status'),
    path('map_update_status/',views.map_update_status,name='map_update_status'),
    path('update_api/',views.update_api,name='update_api'),
]