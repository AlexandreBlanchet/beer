from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('create', views.create, name="create"),
    path('login', views.login, name="login"),
]