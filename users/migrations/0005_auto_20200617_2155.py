# Generated by Django 3.0.5 on 2020-06-17 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200617_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='subject',
            new_name='classes',
        ),
    ]
