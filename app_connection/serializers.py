import datetime
from rest_framework import serializers
from mainpage.models import *




class stationserializer(serializers.Serializer):
    statid = serializers.CharField(max_length=8)
    statnm = serializers.CharField(max_length=100)
    lat = serializers.FloatField(default=0.0)
    lng = serializers.FloatField(default=0.0)
    addr = serializers.CharField(max_length=150)

