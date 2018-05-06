
from datetime import date
from django.db import models
import datetime


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=64, default=None, blank=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Place(models.Model):
    name = models.CharField(max_length=64, blank=False, null=True)
    street = models.CharField(max_length=64, blank=False, null=True)
    building_num = models.IntegerField(blank=True, null=True)
    underground_station = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"


class Event(models.Model):
    event_name = models.CharField(max_length=128, blank=False, default=None)
    description = models.TextField(max_length=1024, blank=True, default=None)
    type = models.ForeignKey(Type, blank=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    poster = models.ImageField(upload_to='sharks-blog/static/media/events_gallery/posters', blank=False, null=True)
    time = models.TimeField(auto_now=False, blank=True, default=datetime.time(19, 00, 00))
    place = models.ForeignKey(Place, blank=False, null=True, on_delete=models.DO_NOTHING)
    price = models.IntegerField(blank=True, default=100)

    @property
    def is_past(self):
        return  self.date < date.today()

    def __str__(self):
        return "%s %s " % (self.type.name, self.event_name)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventImage(models.Model):
    event = models.ForeignKey(Event, blank=False, default=None, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sharks-blog/static/media/events_gallery/gallery')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

