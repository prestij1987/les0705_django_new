from django.urls import path

from lotery import views

urlpatterns = [
    path('', views.index)
]
