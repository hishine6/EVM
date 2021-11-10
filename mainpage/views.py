from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from EVM.settings import KAKAO_API_KEY
from mainpage.get_api import get_data
from mainpage.models import *


def main_page(request):
    return render(request, 'main_page.html')

def update_api(request):
    if (request.method == 'POST'):
        ret = get_data()
    else:
        return render(request,'update_api.html')

def add_station(request):
    if(request.method=='POST'):
        return 0
    else:
        context={}
        return render(request,'add_station.html',context)

def map_status(request):
    # 1. map center lat, lng
    _lat = 37.54989794096065
    _lng = 126.94100229832952

    context = {'Key' : KAKAO_API_KEY,
               'lat' : _lat,
               'lng' : _lng}
    if (request.method == 'POST'):
        ret = get_data()
    return render(request, 'map_status.html',context)

def list_status(request):
    stations = {'stations': charge_station.objects.filter(zcode='42')}
    #stations = {'stations': charge_station.objects.all()}


    return render(request, 'list_status.html', stations)

def map_update_status(request):
    if request.method == 'GET':
        # 범위 내의 좌표들을 읽어와서 보내준다.
        _x_low = request.GET.get('x_low', '')
        _y_low = request.GET.get('y_low', '')
        _x_high = request.GET.get('x_high', '')
        _y_high = request.GET.get('y_high', '')

        _temp = charge_station.objects.filter(lng__gte=_x_low,lng__lte=_x_high,lat__gte=_y_low,lat__lte=_y_high)
        context = {}
        for temp in _temp:
            context[temp.statid] = {'statid': temp.statid,
                                    'lat': temp.lat,
                                    'lng': temp.lng}
        return JsonResponse(context)


