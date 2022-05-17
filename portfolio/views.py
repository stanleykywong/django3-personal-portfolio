from django.shortcuts import render

from .models import Project     # 8i---in views.py, add:

# Create your views here.

# 8f---portfolio folder > views.py, add view:
def home(request):
    projects = Project.objects.all()   # 8j---in views.py, add:
    return render(request, 'portfolio/home.html', {'projects':projects})    #8k---add codes: , {'projects':projects}, to show all objects from above code line
