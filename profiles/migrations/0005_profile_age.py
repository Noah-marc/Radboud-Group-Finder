# Generated by Django 3.2.13 on 2022-05-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_study_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
