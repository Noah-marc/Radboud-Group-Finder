# Generated by Django 4.0.4 on 2022-05-31 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datastructures', '0004_choices_profile_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='choices',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]
