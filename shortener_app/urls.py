from django.urls import path
from shortener_app import views

urlpatterns = [
    path('', views.create, name='home'),
    path('create/', views.create, name='create'),
    path('<uri>/', views.redirect, name='redirect'),
]
