"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# 11f---as in 11a, there used "include",
# to fix error, add "include" in personal_portfolio/urls.py:
# from django.urls import path
from django.urls import path, include

# 8b---in personal_portfolio, urls.py, add:
from django.conf.urls.static import static
from django.conf import settings

# 8d---to fix error, in personal_portfolio, urls.py, add:
from portfolio import views

# 8e---to fix error, in personal_portfolio, urls.py, add:
# 11a---personal_portfolio folder > urls.py, add to urlpatterns = [ ]: path('blog/', include('blog.urls')),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  #''---means root: localhost:8000/
    path('blog/', include('blog.urls')),
]

# 8b---in personal_portfolio, urls.py, add:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
