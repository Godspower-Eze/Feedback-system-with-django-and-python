from django.contrib import admin
from django.urls import path, include
from .views import create_student_user, create_teacher_user, login_user, profile

urlpatterns = [
    path('createstudent/', create_student_user, name='create_student_user'),
    path('createteacher/', create_teacher_user, name='create_teacher_user'),
    path('login/', login_user, name='login'),
    path('profile/', profile, name='profile')

]
