from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

degree = [
    ('bsc', 'Bsc'),
    ('msc', 'Msc'),
    ('phd', 'Phd')
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

    teacher = models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'is_teacher':True}, primary_key=True)
    other_names = models.CharField('Other Names', max_length=100)
    teacher_image = models.ImageField(default='default.jpg', upload_to='teachers_images')
    qualification = models.CharField('Qualification', max_length=100, choices=degree)
    relationship = models.CharField('Relationship Status', max_length=100, choices=status)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.first_name} {self.teacher.last_name} {self.qualification}"


class Classes(models.Model):
    class Meta:
        verbose_name_plural = 'Classes'

    class_name = models.CharField(max_length=100, choices=classes)
    num_of_students = models.IntegerField(blank=True, null=True)
    teachers = models.ManyToManyField(TeachersProfile, blank=True)

    def __str__(self):
        return self.class_name


class StudentProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Student Profile'

    student = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_student':True}, primary_key=True)
    other_names = models.CharField('Other Names', max_length=100, blank=True)
    student_image = models.ImageField(default='default.jpg', upload_to='student_images')
    guardians_name = models.CharField('Name Of Guardian', max_length=150, blank=True)
    teachers = models.ManyToManyField(TeachersProfile, blank=True)
    my_class = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.my_class.class_name}"


class Subjects(models.Model):
    class Meta:
        verbose_name_plural = 'Subjects'

    subject_name = models.CharField(max_length=100)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(TeachersProfile, blank=True)
    students = models.ManyToManyField(StudentProfile)

    def __str__(self):
        return self.subject_name


@receiver(post_save, sender=StudentProfile)
def student_created(sender, instance, created, **kwargs):
    if created:
        user = Classes.objects.get(id=instance.my_class.id)
        user.num_of_students += 1
        user.save()


@receiver(post_delete, sender=StudentProfile)
def student_deleted(sender, instance, **kwargs):
    user = Classes.objects.get(id=instance.my_class.id)
    user.num_of_students -= 1
    user.save()
