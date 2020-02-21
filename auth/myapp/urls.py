from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
]