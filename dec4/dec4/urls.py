from django.urls import path
from dec4app import views

urlpatterns = [
    path('', views.index),
    path('register', views.af_reg),
    path('login', views.login),
]