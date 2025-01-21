from django.urls import path
from django.urls.conf import include
from web_project import views


urlpatterns = [
    path("", views.Koti, name='koti'),
   
]