from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentCreate, UserCreate, TeacherCreate, SurveyAnswer
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SurveyInfo, SurveyAnswers, SurveyTextareaAnswer


@transaction.atomic
def create_student_user(request):
    if request.user.is_authenticated:
        return redirect('profile')
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
            return redirect('login')
    else:
        form1 = UserCreate()
        form2 = StudentCreate()
    return render(request, 'surveysystem/create_student_user.html', context)


def create_teacher_user(request):
    if request.user.is_authenticated:
        return redirect('profile')
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
            return redirect('login')
    return render(request, 'surveysystem/create_teacher_user.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back. You have successfully logged in')
            return redirect('profile')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('.')
    return render(request, 'surveysystem/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'surveysystem/profile.html')


@login_required
def surveypage(request):
    if request.user.is_authenticated and not request.user.is_student:
        return redirect('profile')
    surveys = SurveyInfo.objects.all()
    context = {
        'surveys': surveys
    }
    return render(request, 'surveysystem/surveypage.html', context)


@login_required
def survey(request, survey_id):
    if request.user.is_authenticated and not request.user.is_student:
        return redirect('profile')
    form = SurveyAnswer()
    survey_details = get_object_or_404(SurveyInfo, survey_title=survey_id)
    if request.method == 'POST':
        for questions in survey_details.surveyq_set.all():
            name = 'choice' + str(questions.id)
            choice = request.POST.get(name)
            teacher = request.POST.get('teacher')
            textarea = request.POST.get('textarea')
            SurveyAnswers.objects.create(student=request.user.studentprofile,
                                         survey_question=questions,
                                         normal_answer=choice,
                                         teacher_id=teacher
                                         )
        SurveyTextareaAnswer.objects.create(
            student=request.user.studentprofile,
            teacher_id=teacher,
            survey_id=survey_details.id,
            survey_textarea_answer=textarea
        )
        return redirect('surveypage')
    context = {
        'survey_details': survey_details,
        'form': form
    }
    return render(request, 'surveysystem/survey.html', context)
