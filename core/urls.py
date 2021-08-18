from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('application/<int:pk>', views.appview, name='appview'),   

]