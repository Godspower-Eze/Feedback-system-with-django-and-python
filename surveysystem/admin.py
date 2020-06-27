from django.contrib import admin
from .models import (User,
                     TeachersProfile,
                     StudentProfile,
                     Class,
                     Subjects,
                     SurveyInfo,
                     SurveyQ,
                     SurveyChoices,
                     SurveyAnswers,
                     SurveyTextareaAnswer)


class SurveyChoicesInline(admin.StackedInline):
    model = SurveyChoices
    extra = 3


class SurveyQAdmin(admin.ModelAdmin):
    inlines = [SurveyChoicesInline]


admin.site.register(User)
admin.site.register(TeachersProfile)
admin.site.register(StudentProfile)
admin.site.register(Class)
admin.site.register(Subjects)
admin.site.register(SurveyInfo)
admin.site.register(SurveyQ, SurveyQAdmin)
admin.site.register(SurveyAnswers)
admin.site.register(SurveyTextareaAnswer)
