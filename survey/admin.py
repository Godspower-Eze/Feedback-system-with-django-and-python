from django.contrib import admin
from .models import SurveyQ, SurveyInfo, SurveyAnswers, SurveyChoices

admin.site.register(SurveyInfo)
admin.site.register(SurveyQ)
admin.site.register(SurveyAnswers)
admin.site.register(SurveyChoices)
