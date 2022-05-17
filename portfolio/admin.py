from django.contrib import admin

# Register your models here.

# 7a---personal_portfolio_project/portfolio/admin.py, register your models
from .models import Project

# 7a---after it, PORTFOLIO Projects is shown up in Admin Page, and you may Add project
admin.site.register(Project)
