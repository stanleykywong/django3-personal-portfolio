from django.contrib import admin

# Register your models here.

# 12c---in blog/admin.py, add:
from .models import Blog

# after it, PORTFOLIO Projects is shown up in Admin Page, and you may Add project
admin.site.register(Blog)
