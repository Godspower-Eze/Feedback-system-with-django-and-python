from django.contrib import admin
from .models import (User,
                     TeachersProfile,
                     StudentProfile,
                     Class,
                     Subjects)

admin.site.register(User)
admin.site.register(TeachersProfile)
admin.site.register(StudentProfile)
admin.site.register(Class)
admin.site.register(Subjects)
