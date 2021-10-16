from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.one, name='one'),
]
