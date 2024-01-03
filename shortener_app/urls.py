from django.urls import path
from shortener_app import views

urlpatterns = [
    path('', views.current_datetime, name='home'),
]
