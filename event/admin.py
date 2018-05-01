from django.contrib import admin
from .models import *

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0

class TypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Type._meta.fields]

    class Meta:
        model = Type

admin.site.register(Type, TypeAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Place._meta.fields]

    class Meta:
        model = Place

admin.site.register(Place, PlaceAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]
    list_filter = ['type']
    inlines = [EventImageInline]

    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)

class EventImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventImage._meta.fields]

    class Meta:
        model = EventImage

admin.site.register(EventImage, EventImageAdmin)
