# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Group(models.Model):
    # класс обяз-но наследуются от Model, который в модуле models, имя таблицы = имя приложения_имя класса
    # Student Model"""
    #создаем таблицу Студенты, благодаря Django ORM мы описываем класс, в который отображается таблица БД

    class Meta(object):
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"
    
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Название")
        # u - юникод

    leader = models.OneToOneField('Student',
       blank=True,
       null=True,
       verbose_name=u"Староста",
       on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Дополнительные примечания")

    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u"%s" % (self.title,)
        