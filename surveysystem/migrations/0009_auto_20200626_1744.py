# Generated by Django 3.0.5 on 2020-06-26 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveysystem', '0008_auto_20200624_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyanswers',
            name='student',
        ),
        migrations.AddField(
            model_name='surveyinfo',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='surveysystem.StudentProfile'),
        ),
        migrations.AlterField(
            model_name='surveyinfo',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='surveysystem.TeachersProfile'),
        ),
    ]