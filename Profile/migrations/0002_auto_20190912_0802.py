# Generated by Django 2.1.5 on 2019-09-12 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=10, verbose_name='Пол')),
                ('date_born', models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения')),
                ('photo', models.FileField(upload_to='static/photo')),
                ('weight', models.FloatField(verbose_name='Вес')),
                ('height', models.FloatField(verbose_name='Рост')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(verbose_name='КилоКалории'),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbohydrates',
            field=models.FloatField(verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='food',
            name='fats',
            field=models.FloatField(verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='food',
            name='proteins',
            field=models.FloatField(verbose_name='Белки'),
        ),
        migrations.AlterField(
            model_name='userfood',
            name='amount_food',
            field=models.FloatField(default='100', verbose_name='К-во продукта'),
        ),
        migrations.AlterField(
            model_name='userfood',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
