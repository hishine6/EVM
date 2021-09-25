from urllib import parse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from EVM.settings import DATA_API_KEY
from mainpage.models import charge_station
import datetime

serviceKey_utf8 = DATA_API_KEY
serviceKey = parse.unquote(serviceKey_utf8, 'UTF-8')


# TODO
# 1. Read XML from multiple api? No, only one API
# 2. Parse the data and save the needed factors. Done
# 3. create a Database for the required project. Done
# 4. Set CSS, label html.

def get_data():
    url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
    for i in range(1,10):
        params = {
            "ServiceKey": serviceKey,
            "pageNo": i,
            "numOfRows": 9999,
        }
        res = requests.get(url, params=params)
        xml = BeautifulSoup(res.text, "lxml")

        items = xml.find("items")
        for item in items:
            item_dict = {
                'statnm': item.find("statnm").text, # name
                'statid': item.find("statid").text,  # ID
                'chgerid': item.find("chgerid").text,    # Charger ID
                'chgertype': item.find("chgertype").text,    # Charger Type
                'addr': item.find("addr").text,  # Address
                'lat': float(item.find("lat").text),    # Lat
                'lng': float(item.find("lng").text),    # Lng
                'usetime': item.find("usetime").text,    # Time
                'busiid': item.find("busiid").text,  # 기관 ID
                'businm': item.find("businm").text,  # 기관 이름
                'busicall': item.find("busicall").text, # 연락처
                'stat': int(item.find("stat").text), # 상태
                'statupddt': item.find("statupddt").text,
                'zcode': item.find("zcode").text,
                'parkingfree': item.find("parkingfree").text,
                'note': item.find("note").text,
            }
            _usetime_start = 0
            _usetime_end = 0
            _parking_free = False
            if(item_dict['parkingfree']=='Y'):
                _parking_free = True
            if(item_dict['statupddt'] != ''):
                _statupddt = datetime.datetime(int(item_dict['statupddt'][0:4]),int(item_dict['statupddt'][4:6]),int(item_dict['statupddt'][6:8]),
                                           int(item_dict['statupddt'][8:10]),int(item_dict['statupddt'][10:12]),int(item_dict['statupddt'][12:14]))
            else:
                _statupddt = datetime.datetime.now()

            _charge_station = charge_station(statid=item_dict['statid'],
                                                 statnm = item_dict['statnm'],
                                                 chgerid=item_dict['chgerid'],
                                                 chagertype=item_dict['chgertype'],
                                                 addr=item_dict['addr'],
                                                 lat=item_dict['lat'],
                                                 lng = item_dict['lng'],
                                                 usetime_start=_usetime_start,
                                                 usetime_end=_usetime_end,
                                                 busiid=item_dict['busiid'],
                                                 businm=item_dict['businm'],
                                                 busicall=item_dict['busicall'],
                                                 stat=item_dict['stat'],
                                                 statupddt=_statupddt,
                                                 zcode=item_dict['zcode'],
                                                 parkingfree=_parking_free,
                                                 note=item_dict['note'])
            _charge_station.save()
        print(i)
        print(charge_station.objects.count())
    return res
