from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    search_fields = ['user']
    list_filter = ['event']

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)
