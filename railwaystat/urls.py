from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('Home', views.Home, name='Home'),
    path('TrainStatus', views.TrainStat, name='TrainStatus'),
    path('TrainName', views.CheckTrainStatus, name='TrainName'),
    path('checkview', views.checkview, name='checkview'),
    path('verify', views.verify, name='verify')
]