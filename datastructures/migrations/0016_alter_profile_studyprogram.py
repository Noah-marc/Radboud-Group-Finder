# Generated by Django 4.0.4 on 2022-06-07 13:18

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datastructures', '0015_remove_membership_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='studyProgram',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Computing Science', 'Computing Science'), ('Mathematics', 'Mathematics')], default='', max_length=29),
        ),
    ]
