from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'converters'),
    path('lengthconv',views.lengthconv, name='lengthconv'),
    path('capacityconv',views.capacityconv, name='capacityconv'),
    path('heatconv',views.heatconv, name='heatconv'),
    path('exchangeconv',views.exchangeconv, name='exchangeconv'),
]