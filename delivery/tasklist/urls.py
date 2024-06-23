
from django.urls import path

from tasklist import views


urlpatterns = [
    path('', views.func_new),
   # path('home/', about)
]