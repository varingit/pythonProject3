from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('LWdp/', views.LWdp, name='LWdp'),
    path('MWdp/', views.MWdp, name='MWdp'),
    path('GWdp/', views.GWdp, name='GWdp'),

    ]