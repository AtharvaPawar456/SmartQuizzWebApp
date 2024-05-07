from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quiz/", views.quiz, name="quiz"),
    path("quiz_completed/", views.quiz_completed, name="quiz_completed"),

    path('reset_quiz/', views.reset_quiz, name='reset_quiz'),
    # path('create/', views.create_question, name='create_question'),
    
    path('head_form/', views.head_form, name='head_form'),
    path('question_form/', views.question_form, name='question_form'),


    path("result/", views.result, name="result"),

    # path("contact/", views.contact, name="ContactUs"),
    # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),

]