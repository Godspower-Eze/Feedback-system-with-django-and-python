from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

degree = [
    ('Bsc', 'Bsc'),
    ('Msc', 'Msc'),
    ('Phd', 'Phd')
]

status = [
    ('single', 'Single'),
    ('married', 'Married')
]

classes = [
    ('JSS1', 'JSS1'),
    ('JSS2', 'JSS2'),
    ('JSS2', 'JSS3')

]


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class TeachersProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Teachers Profiles'

    teacher = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True},
                                   primary_key=True)
    other_names = models.CharField('Other Names', max_length=100)
    teacher_image = models.ImageField(default='default.jpg', upload_to='teachers_images')
    qualification = models.CharField('Qualification', max_length=100, choices=degree)
    relationship = models.CharField('Relationship Status', max_length=100, choices=status)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.first_name} {self.teacher.last_name} {self.qualification}"


class Class(models.Model):
    class Meta:
        verbose_name_plural = 'Classes'

    class_name = models.CharField(max_length=100, choices=classes)
    num_of_students = models.IntegerField(blank=True, default=0)
    teachers = models.ManyToManyField(TeachersProfile, blank=True)

    def __str__(self):
        return self.class_name


class StudentProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Student Profile'

    student = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True},
                                   primary_key=True)
    other_names = models.CharField('Other Names', max_length=100, blank=True)
    student_image = models.ImageField(default='default.jpg', upload_to='student_images')
    guardians_name = models.CharField('Name Of Guardian', max_length=150, blank=True)
    teachers = models.ManyToManyField(TeachersProfile, blank=True)
    my_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.my_class.class_name}"


class Subjects(models.Model):
    class Meta:
        verbose_name_plural = 'Subjects'

    subject_name = models.CharField(max_length=100, blank=True)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True)
    teachers = models.ManyToManyField(TeachersProfile, blank=True)

    def __str__(self):
        return self.subject_name


@receiver(post_save, sender=StudentProfile)
def student_created(sender, instance, created, **kwargs):
    if created:
        user = Class.objects.get(id=instance.my_class.id)
        user.num_of_students += 1
        user.save()


@receiver(post_delete, sender=StudentProfile)
def student_deleted(sender, instance, **kwargs):
    user = Class.objects.get(id=instance.my_class.id)
    user.num_of_students -= 1
    user.save()


class SurveyInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Survey Info'

    survey_image = models.ImageField(default='default.png', upload_to='survey_images')
    survey_title = models.CharField(max_length=100)
    survey_info = models.TextField()
    survey_textarea_question = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.survey_title + ' - ' + str(self.id)


class SurveyQ(models.Model):
    class Meta:
        verbose_name_plural = 'Survey Questions'

    survey_info = models.ForeignKey(SurveyInfo, default='', on_delete=models.CASCADE)
    survey_question = models.CharField(max_length=500)

    def __str__(self):
        return self.survey_question + ' - ' + str(self.id)


class SurveyChoices(models.Model):
    class Meta:
        verbose_name_plural = 'Survey Choices'

    survey_question = models.ForeignKey(SurveyQ, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)

    def __str__(self):
        return self.choice + ' - ' + str(self.id)


class SurveyAnswers(models.Model):
    class Meta:
        verbose_name_plural = 'Survey Answers'

    student = models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING, null=True)
    survey_question = models.ForeignKey(SurveyQ, default='', on_delete=models.CASCADE)
    normal_answer = models.CharField(max_length=100, null=True, blank=True)
    teacher = models.ForeignKey(TeachersProfile, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.normal_answer)


class SurveyTextareaAnswer(models.Model):
    class Meta:
        verbose_name_plural = 'Survey Textarea Questions'

    student = models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(TeachersProfile, on_delete=models.DO_NOTHING)
    survey = models.ForeignKey(SurveyInfo, on_delete=models.DO_NOTHING)
    survey_textarea_answer = models.TextField()

    def __str__(self):
        return f"{str(self.student)} - {str(self.teacher)} - {self.survey_textarea_answer}"