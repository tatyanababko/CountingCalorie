# Generated by Django 2.1.5 on 2019-09-17 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_profileuser_dima'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='dima',
        ),
    ]
