# 11c---copy and modify codes from personal_portfolio/urls.py to  personal_portfolio_project/blog/urls.py

from django.urls import path
from . import views

# 16h---personal_portfolio_project/blog/urls.py, add:
app_name = 'blog'

# ''---means NO subroot under: localhost:8000/blog/
# if 'hello'---means there's a subroot; we need go to: localhost:8000/blog/hello, to show the contents
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),     # 16a---personal_portfolio_project/blog/urls.py, add:
]
