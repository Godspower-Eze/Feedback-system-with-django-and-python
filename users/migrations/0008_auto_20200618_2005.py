# Generated by Django 3.0.5 on 2020-06-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200618_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='num_of_students',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]