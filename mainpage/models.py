from django.db import models

class charge_station(models.Model):
    statid = models.CharField(max_length=8)
    statnm = models.CharField(max_length=100)
    chgerid = models.CharField(max_length=2)
    chagertype = models.CharField(max_length=2)
    addr = models.CharField(max_length=150)
    lat = models.FloatField(default = 0.0)
    lng = models.FloatField(default = 0.0)
    usetime_start = models.PositiveIntegerField(default=0)
    usetime_end = models.PositiveIntegerField(default=0)
    busiid = models.CharField(max_length=2)
    businm = models.CharField(max_length=50)
    busicall = models.CharField(max_length=20)
    stat = models.PositiveIntegerField(default = 0)
    statupddt = models.DateTimeField()
    zcode = models.CharField(max_length=2)
    parkingfree = models.BooleanField()
    note = models.CharField(max_length=200)

    class Meta:
        unique_together = (("statid"),("chgerid"),)
