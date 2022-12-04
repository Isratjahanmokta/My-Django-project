from django.urls import path
from App_post import views

app_name = 'App_post'

urlpatterns = [
    path("", views.home, name='home'),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('unliked/<pk>/', views.unliked, name ='unliked_post'),
]