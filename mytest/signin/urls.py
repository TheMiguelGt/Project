#django 
from django.urls import path 

#views 
from . import views 


#config url 
urlpatterns = [
    path('choose', views.signin, name='choose'),
    path('choose/teach', views.teach, name='teach'),
    path('choose/student', views.student, name='student'),
    path('choose/familiar', views.familiar, name='familiar'),
]
