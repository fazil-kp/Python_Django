from django.urls import path
from . import views

urlpatterns = [
    path('',views.fan,name='fun'),
    path('datas',views.datas,name='datas')
]
