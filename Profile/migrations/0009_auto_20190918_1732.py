# Generated by Django 2.1.5 on 2019-09-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_auto_20190918_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='photo',
            field=models.FileField(default='static/photo/2cat.jpeg', upload_to='static/photo'),
        ),
    ]