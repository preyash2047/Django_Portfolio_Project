from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('', views.all_blog, name = "all_blog"),
    path('<int:blog_id>', views.blog, name="detail"),
]