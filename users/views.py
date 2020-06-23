from django.shortcuts import render, redirect
from .forms import StudentCreate, UserCreate, TeacherCreate
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@transaction.atomic
def create_student_user(request):
    form1 = UserCreate()
    form2 = StudentCreate()
    context = {
        'form1': form1,
        'form2': form2
    }
    if request.method == 'POST':
        form1 = UserCreate(request.POST)
        form2 = StudentCreate(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_student = True
            user.save()
            add = form2.save(commit=False)
            add.student = user
            add.save()
            teachers = form2.cleaned_data.get('teachers')
            add.teachers.set(teachers)
            add.save()
            return redirect('.')
    else:
        form1 = UserCreate()
        form2 = StudentCreate()
    return render(request, 'users/create_student_user.html', context)


def create_teacher_user(request):
    form1 = UserCreate()
    form2 = TeacherCreate()
    context = {
        'form1': form1,
        'form2': form2
    }
    if request.method == 'POST':
        form1 = UserCreate(request.POST)
        form2 = TeacherCreate(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_teacher = True
            user.save()
            user1 = form2.save(commit=False)
            user1.teacher = user
            user1.save()
            subjects = form2.cleaned_data.get('subjects')
            user1.subjects_set.set(subjects)
            user1.save()
            return redirect('.')
    return render(request, 'users/create_teacher_user.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Welcome back. You have successfully logged in')
            return redirect('profile')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('.')
    return render(request, 'users/login.html')


@login_required
def profile(request):
    return render(request,'users/profile.html')
