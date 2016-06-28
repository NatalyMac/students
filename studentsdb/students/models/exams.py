# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Exam(models.Model):
	# класс обяз-но наследуются от Model, который в модуле models, имя таблицы = имя приложения_имя класса
    # Student Model"""
    #создаем таблицу Студенты, благодаря Django ORM мы описываем класс, в который отображается таблица БД

    class Meta(object):
        verbose_name = u"Экзамен"
        verbose_name_plural = u"Экзамены"
    
    exam_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Название предмета")
        # u - юникод

    teach_name = models.CharField(
       max_length=256,
       blank=False,
       verbose_name=u"Преподаватель")

    exam_group = models.ManyToManyField('Group',
       verbose_name=u"Група",
       blank=False,
       #null=True при таком типе взаимозвязи нулевое значение бесмысленно, мало того он еще и ругается;))
       )
# связь много-много, поскольку разные группы могут сдавать  одни и те же экзамены, 
    exam_date = models.DateField(
       blank=False,
       verbose_name=u"Дата экзамена",
       null=True)
 
    notes = models.TextField(
        blank=True,
        verbose_name=u"Дополнительные примечания")

    def __unicode__(self):
        return u"%s %s" % (self.exam_name, self.teach_name)