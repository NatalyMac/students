# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
	# класс обяз-но наследуются от Model, который в модуле models, имя таблицы = имя приложения_имя класса
    # Student Model"""
    #создаем таблицу Студенты, благодаря Django ORM мы описываем класс, в который отображается таблица БД

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенты"
    
    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Имя")
        # u - юникод

    last_name = models.CharField(
       max_length=256,
       blank=False,
       verbose_name=u"Фамилия")

    middle_name = models.CharField(
       max_length=256,
       blank=True,
       verbose_name=u"Отчество",
       default='')
    
    student_group = models.ForeignKey('Group',
       verbose_name=u"Група",
       blank=False,
       null=True,
       on_delete=models.PROTECT)  
    
    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата рождения",
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)
        # image файлы не сохраняются в БД, БД хранит имя файла, файлы хранятся в файловой системе. 
        # Нtобходимы настройки пути к папке, где будут хранится медиа-файлы

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Билет")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Дополнительные примечания")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    # blank - указываем обязательное ли поле для заполнения в форме
    # verbose_name - название поля в польз. интерфейсе, если нет - то имя атрибута выводится
    # для поля varchar обязательно указание длины
    # null=true - поле может быть пустым в БД, blank - для формы


