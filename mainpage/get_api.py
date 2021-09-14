from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup
from EVM.settings import DATA_API_KEY

serviceKey_utf8 = DATA_API_KEY
serviceKey = unquote(serviceKey_utf8, 'UTF-8')

def get_data():
    url = 'http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList'
    params = {
        "ServiceKey": serviceKey,
        "pageNo": 1,
        "numOfRows": 5,
    }
    res = requests.get(url, params=params)
    xml = res.text
    return res
