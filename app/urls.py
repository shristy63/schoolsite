from .views import *
from django.urls import path

urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),

    path('course/',course,name="course"),
    path('course/add/',course_add,name="course_add"),
    path('course/edit/<int:id>/',course_edit,name="course_edit"),
    path('course/delete/<int:id>/',course_delete,name="course_delete"),
]

