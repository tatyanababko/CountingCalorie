from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


CATEGORIES_FOOD = (
    (1, "Предложен"),
    (2, "Утвержден")
)


class ProfileUser(models.Model):
    objects = None
    username = models.ForeignKey(User, verbose_name='Пользователь', db_index=True, on_delete=models.CASCADE)
    date_born = models.DateField(verbose_name="Дата рождения", default=timezone.now)
    weight = models.FloatField(verbose_name="Вес")
    height = models.FloatField(verbose_name="Рост")
    photo = models.FileField(upload_to='static/photo', default='static/photo/Dogg.jpeg')

    def __str__(self):
        return f"{self.username} ({self.date_born})"


class Food(models.Model):
    objects = None
    name_product = models.CharField(max_length=256, unique=True, verbose_name="Название продукта")
    proteins = models.FloatField(verbose_name="Белки")
    fats = models.FloatField(verbose_name="Жиры")
    carbohydrates = models.FloatField(verbose_name="Углеводы")
    calories = models.FloatField(verbose_name="КилоКалории")
    weight = models.FloatField(verbose_name="Вес продукта гр.", default="100.0")
    categories = models.IntegerField(choices=CATEGORIES_FOOD, default=1, verbose_name="Категория")

    def __str__(self):
        return f"{self.name_product}"


class UserFood(models.Model):
    objects = None
    username = models.ForeignKey(User, verbose_name='Пользователь', db_index=True, on_delete=models.CASCADE)
    name_product = models.ForeignKey(Food, db_index=True, on_delete=models.CASCADE, verbose_name='Название продукта')
    amount_food = models.FloatField(verbose_name="К-во продукта", default="100")
    data_time_add_product = models.DateField(verbose_name="Дата продукта", default=timezone.now)
    count_calories = models.FloatField(verbose_name="Ккал расчет")

    @property
    def food_calories(self):
        result = Food.objects.filter(name_product__name_product=self.name_product).calories
        return result

    def save(self, *args, **kwargs):
        self.count_calories = (self.amount_food * self.food_calories) / 100
        super(UserFood, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}: {self.name_product} = {self.amount_food}гр. " \
               f"( {self.data_time_add_product:%Y-%m-%d} )"
