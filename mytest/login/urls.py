#django 
from django.urls import path, include

#views 
from . import views 


#config url 
urlpatterns = [
    path('', views.login, name='login'),
]
