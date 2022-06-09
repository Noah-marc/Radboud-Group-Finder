# Generated by Django 3.2.13 on 2022-06-09 13:57

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datastructures', '0017_auto_20220609_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.CharField(choices=[('Calculus and Probability Theory', 'Calculus and Probability Theory'), ('Hacking in C', 'Hacking in C')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Calculus and Probability Theory', 'Calculus and Probability Theory'), ('Hacking in C', 'Hacking in C')], default='', max_length=44),
        ),
    ]