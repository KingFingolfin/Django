from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
    path('', views.homepage, name='HomePage'),
    path('search', views.search, name='Search'),# here
    path('single_test/<int:id>', views.single_test, name='Single_Test'),# here
    path('contact_us', views.ContactUs, name='Contact_Us'),# here
    path('politic', views.Politic, name='Politic'),# here
    path('science', views.Science, name='Science'),# here
    path('art', views.Art, name='Art'),# here
    path('history', views.History, name='History'),# here
    path('other', views.Other, name='Other'),# here
]
