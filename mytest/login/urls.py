#django 
from django.urls import path, include

#views 
from . import views 


#config url 
urlpatterns = [
    path('login', views.login, name='login'),
]
