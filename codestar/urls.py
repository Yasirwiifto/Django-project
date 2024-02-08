from django.contrib import admin
from django.urls import path
from blog.views import my_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_blog, name='blog'),
]
