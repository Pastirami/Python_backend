from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('index/',views.index, name="index"),
    path('show/<titre>', views.show, name="show"),
    path('create/', views.create, name="create"),
    path('about/', views.create, name="about"),
]