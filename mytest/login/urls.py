#django 
from django.urls import path, include

#views 
from . import views 


#config url 
urlpatterns = [
    path('choose', views.choose, name='choose acount'),
    path('choose/teach', views.teach, name='teach'),
    path('choose/student', views.student, name='student'),
    path('choose/familiar', views.familiar, name='familiar'),
]
