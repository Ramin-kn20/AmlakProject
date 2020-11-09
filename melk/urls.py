from django.urls import path
from . import views

app_name = 'AMLAKAPP'
urlpatterns = [
    path('', views.melk_list, name='list'),
    path('<slug>', views.melk_details, name='slug')
]
