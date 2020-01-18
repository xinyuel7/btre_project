from django.urls import path
from . import views # path is attached to a method(function) of a view 
urlpatterns = [ #homepage
    path('', views.index, name ='index'),
    path('about', views.about, name ='about'),
]