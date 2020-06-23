from django import forms
from .models import User, StudentProfile, TeachersProfile, Subjects
from django.contrib.auth.forms import UserCreationForm


class UserCreate(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']


class StudentCreate(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['other_names', 'guardians_name', 'student_image', 'my_class']

    teachers = forms.ModelMultipleChoiceField(queryset=TeachersProfile.objects.all()
                                              ,required=False)


class TeacherCreate(forms.ModelForm):
    class Meta:
        model = TeachersProfile
        fields = ['other_names', 'teacher_image', 'qualification', 'relationship']

    subjects = forms.ModelMultipleChoiceField(label='Subjects Taught',queryset=Subjects.objects.all(),
                                              required=True)