# Generated by Django 3.0.5 on 2020-06-26 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveysystem', '0014_remove_surveytextareaanswer_surveyq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveytextareaanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='surveysystem.StudentProfile'),
        ),
        migrations.AlterField(
            model_name='surveytextareaanswer',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='surveysystem.SurveyInfo'),
        ),
        migrations.AlterField(
            model_name='surveytextareaanswer',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='surveysystem.TeachersProfile'),
        ),
    ]
