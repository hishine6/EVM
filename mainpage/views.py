from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from EVM.settings import KAKAO_API_KEY
from mainpage.get_api import get_data
from mainpage.models import *
from django.core.paginator import Paginator


def main_page(request):
    return render(request, 'main_page.html')

@csrf_exempt
def update_api(request):
    if (request.method == 'POST'):
        ret = get_data()
    return render(request,'update_api.html')

def add_station(request):
    if(request.method=='POST'):
        return 0
    else:
        context={}
        return render(request,'add_station.html',context)

def map_status(request):
    _statid = request.GET.get('statid','')
    if _statid == '':
        _lat = 37.54989794096065
        _lng = 126.94100229832952
    else:
        _station = charge_station.objects.get(statid=_statid)
        _lat = _station.lat
        _lng = _station.lng

    context = {'Key' : KAKAO_API_KEY,
               'lat' : _lat,
               'lng' : _lng}
    return render(request, 'map_status.html',context)

def list_status(request):
    page = request.GET.get('page',1)
    _stations = charge_station.objects.all()
    paginator = Paginator(_stations, 15)
    stations = {'stations': paginator.get_page(page)}
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


