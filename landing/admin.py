from django.contrib import admin
from .models import *

class UserInline(admin.TabularInline):
    model = User
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    search_fields = ['surname', 'name', 'email']

    class Meta:
        model = User

admin.site.register(User, UserAdmin)

class OrgAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Org._meta.fields]
    search_fields = ['surname', 'name', 'email']

    class Meta:
        model = Org

admin.site.register(Org, OrgAdmin)