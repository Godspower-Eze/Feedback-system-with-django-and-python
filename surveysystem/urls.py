from django.contrib import admin
from django.urls import path, include
from .views import (create_student_user,
                    create_teacher_user,
                    login_user,
                    logout_user,
                    profile,
                    survey,
                    surveypage)

urlpatterns = [
    path('createstudent/', create_student_user, name='create_student_user'),
    path('createteacher/', create_teacher_user, name='create_teacher_user'),
    path('', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('surveypage/', surveypage, name='surveypage'),
    path('survey/<str:survey_id>', survey, name='survey')

]
