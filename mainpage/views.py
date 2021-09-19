from django.http import HttpResponse
from django.shortcuts import render

from EVM.settings import KAKAO_API_KEY
from mainpage.get_api import get_data


def main_page(request):
    return render(request, 'main_page.html')



def map_status(request):
    context = {'Key' : KAKAO_API_KEY}
    if (request.method == 'POST'):
        ret = get_data()

    return render(request, 'map_status.html',context)