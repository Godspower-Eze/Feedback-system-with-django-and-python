# Generated by Django 3.0.5 on 2020-06-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200618_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='class_name',
            field=models.CharField(choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS2', 'JSS3')], max_length=100),
        ),
    ]
