# Generated by Django 4.0.4 on 2022-05-31 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastructures', '0009_alter_group_course_alter_profile_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='studyProgram',
            field=models.CharField(choices=[('Computing Science', 'Computing Science'), ('Mathematics', 'Mathematics')], default='', max_length=100),
        ),
    ]