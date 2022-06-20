#django 
from django.urls import path 

#views 
from . import views 


#config url 
urlpatterns = [
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('privacity', views.privacity, name='privacity'),
    path('start', views.contact, name='Start Now'),
]
