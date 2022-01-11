from django.db import models
from django.utils.text import slugify
from django.urls import reverse



class Models(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    sum_money = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Models, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('url_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - (rating: {self.rating}% - {self.year}year - {self.sum_money} money)'

# ссылка на БД https://sqlitebrowser.org/dl/
# в файле models создаем класс
# from django.db import models
#
# class Models(models.Model):
#     name = models.CharField(max_length=40)
#     rating = models.IntegerField()
# первый раз запустить сервер manage.py runserver
#
# и в терминале пишем команду
# python manage.py makemigrations
# и после
# python manage.py migrate    (таблица из класса появится в БД)
#
# ЗАПОЛНЯЕМ ТАБЛИЦУ В БД
#
# через настройки установить пакет ipython и django-exeptions (подсказки в терминале нужно будет добавить
# приложение django_extensions в настройку файла settings.py INSTALLED_APPS)
#
# python manage.py shell_plus --print-sql
#
# Models(name='Kong', rating=80).save()
#
# ВЫБИРАЕМ ЗАПИСИ В БД(SELECT)
#
# если закрыт терминал, то заново запускаем shell и imoprt (from movie_app.models import Models)
# python manage.py shell_plus --print-sql
# Models.objects.all()
# a = Models.objects.all()[:2] - можно делать срезы
# a.name
# a.rating
#
# ИЗМИНЕНИЕ И УДАЛЕНИЕ ЗАПИСИ ИЗ БД(DEL и EDIT)
#
# добавим два столбца
#     year = models.IntegerField(null=True) - в скобках обязательно для заполнения
#     sum_money = models.IntegerField(default=10000000) - в скобках обязательно для заполнения, любое значение int
# python manage.py makemigrations
# и после
# python manage.py migrate
# python manage.py shell_plus --print-sql
# from movie_app.models import Models
# Models.objects.all()
# a = Models.objects.all()[1]
# a.year  = 1356
# a.sum_money = 56564546
# a.save()
# Models.objects.all()[0].delete() - удаление записи по индексу[0]
# Models.objects.create(name='Titanic', rating=85)
# Models.objects.get(id=2) если id не найдет в базе вызовет исключение Models.DoesNotExist,
# если будет два одинаковых значения вызовет исключение
# Models.objects.filter(rating=20), если нужно провести сравние пишем: __gt= (>), __lt=(<), __gte=(>=), __lte=(<=)
# Models.objects.exclude(rating=50), не равно != 50
# Models.objects.filter(rating__gt=93, budget__lt=10000000) найти фильм с рейтингом выше 93 И бюджетом менише 1000000
# Models.objects.exclude(year__isnull=True).filter(budget__lt=500000)
# Models.objects.filter(name__icontains='ig') найти фильмы в которых есть сочетание букв ig, contains чувствителен к ригистру
# Models.objects.filter(name__startswith='ti') найти фильмы в которых есть сочетание букв ti в начале слова
# Models.objects.filter(name__endswith='ic')  найти фильмы в которых есть сочетание букв ik заканчичается буквой i
# Models.objects.filter(id__in=[2,4,5]) поиск по списку id__in