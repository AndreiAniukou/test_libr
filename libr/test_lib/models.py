from django.db import models
from django.shortcuts import reverse
# Create your models here.

class User_name(models.Model):
    user_name = models.CharField(max_length=150, db_index=True)#db_index для быстрого поиска
    slug = models.SlugField(max_length=150, unique=True)#разрешает использовать все символы и уникальные индификатры
    #body = models.TextField(blank=True, db_index=True)#blanc чтобы поле было пустым разрешить
    tags = models.ManyToManyField('Tag', blank=True)
    date_create = models.DateTimeField(auto_now_add=True)#auto_now ставит дату при сохранении в бд


    def get_absolute_url(self):
        return reverse('user_detail_url', kwargs={'slug': self.slug}) #генерирует ссылку


    def __str__(self):
        return self.user_name #для вывода


class Tag(models.Model):
    name_tag = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name_tag


class BookName(models.Model):
    book_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body_text = models.TextField(blank=False, db_index=True)

    def get_absolute_url(self):
        return reverse('book_name_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.book_name