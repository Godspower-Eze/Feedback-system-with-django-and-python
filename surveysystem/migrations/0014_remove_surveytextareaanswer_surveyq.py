# Generated by Django 3.0.5 on 2020-06-26 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveysystem', '0013_auto_20200626_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveytextareaanswer',
            name='surveyq',
        ),
    ]
