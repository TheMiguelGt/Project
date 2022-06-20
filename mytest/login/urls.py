#django 
from django.urls import path, include

#views 
from . import views 


#config url 
urlpatterns = [
    path('choose', views.choose, name='choose acount'),
    path('choose/teach', views.teach, name='teach'),
]
