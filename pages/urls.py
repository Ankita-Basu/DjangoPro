from django.urls import path #to define a path

#the idea is to attach a mathod to the path
from .views import HomePageView, AboutPage


urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPage.as_view(), name = 'about'),
]