from django.db import models


class SurveyInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Survey Info'

    survey_image = models.ImageField(default='default.png', upload_to='survey_images')
    survey_title = models.CharField(max_length=100)
    survey_info = models.TextField()
    survey_textarea_question = models.CharField(max_length=200, default='1')

    def __str__(self):
        return self.survey_title + ' - ' + str(self.id)


class SurveyQ(models.Model):
    class Meta:
        verbose_name_plural = 'Survey Questions'

    survey_info = models.ForeignKey(SurveyInfo, default='1', on_delete=models.CASCADE)
    survey_question = models.CharField(max_length=500)

    def __str__(self):
        return self.survey_question + ' - ' + str(self.id)


class SurveyChoices(models.Model):
    survey_question = models.ForeignKey(SurveyQ, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)

    def __str__(self):
        return self.choice + ' - ' + str(self.id)


class SurveyAnswers(models.Model):
    survey_question = models.ForeignKey(SurveyQ, default='1', on_delete=models.CASCADE)
    normal_answer = models.CharField(max_length=100, null=True, blank=True)
    survey_textarea_answer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.normal_answer)

