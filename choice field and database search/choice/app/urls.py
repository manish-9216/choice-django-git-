from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('choice',views.choice,name="choice"),
    path('show',views.show,name="show")
]
