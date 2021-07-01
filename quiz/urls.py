from django.contrib import admin
from django.urls import path
from .views import welcome, result, saveans, quiz

urlpatterns = [

    path('', welcome, name="welcome"),
    path('result/', result, name="result"),
    path('quiz/', quiz, name="quiz"),
    path('saveans/', saveans, name='saveans'),

]
