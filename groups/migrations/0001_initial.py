# Generated by Django 4.0.4 on 2022-05-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.TextField()),
                ('groupCourse', models.TextField()),
            ],
        ),
    ]
