# Generated by Django 5.0.6 on 2024-05-22 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
    ]