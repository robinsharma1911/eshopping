from django.urls import path

from . import views

urlpatterns = [
    path('', views.log_in, name='log_in'),
    path('regi/',views.registration,name='registration'),
    path('logout/',views.logout,name='logout')
]
