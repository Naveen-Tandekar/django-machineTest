from django.contrib import admin
from . models import *


@admin.register(register)
class registeradmin(admin.ModelAdmin):
    list_display=('Mobile','Address','age')
