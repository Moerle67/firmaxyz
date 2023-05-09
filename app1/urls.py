from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('seite2/', views.seite2, name='seite2'),
]