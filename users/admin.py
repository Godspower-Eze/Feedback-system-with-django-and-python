from django.contrib import admin
from .models import (User,
                     TeachersProfile,
                     StudentProfile,
                     Classes,
                     Subjects)

admin.site.register(User)
admin.site.register(TeachersProfile)
admin.site.register(StudentProfile)
admin.site.register(Classes)
admin.site.register(Subjects)
