from django.urls import path
from . import views

# /articles/ ___
urlpatterns = [
    path('', views.index),
    path('<int:article_pk>/', views.detail),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:article_pk>/delete/', views.delete),
]
