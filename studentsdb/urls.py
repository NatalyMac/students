
# coding: utf-8
"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin #все запросы по адресу admin/ обрабатываются этим модулем
from students.views.students import students_list, students_list, students_add, students_edit, students_delete 
from students.views.groups import groups_list, groups_add,groups_edit, groups_delete
from students.views.journal import journal_list, journal_student, journal_update
from students.views.exams import exam_list
from students.views.contact_admin import contact_admin
from .settings import MEDIA_ROOT, DEBUG
#from students import views
urlpatterns = [
	#students url
	url(r'^$', students_list, name='home'),
    # при проверке url-паттерна 'имя домена/' не входит в проверку, поэтому все регулярные выраж. для урлов не содержат имя домена/
    # поэтому urlпаттерн = ^$ - пустая строка, соответствует запросам в корневой адрес www.имя домена/
    url(r'^students/add/$', students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$',students_edit, name='students_edit'), #sid идентификатор студента
    url(r'^students/(?P<sid>\d+)/delete/$',students_delete, name='students_delete'),
    
    #groups link
    url(r'^groups/$', groups_list, name='groups'),
    url(r'^groups/add/$', groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$',groups_edit, name='groups_edit'), #gid идентификатор группы
    url(r'^groups/(?P<gid>\d+)/delete/$',groups_delete,name='groups_delete'),
    
    #journal links
    url(r'^journal/$', journal_list, name='journal'),
    url(r'^journal/(?P<sid>\d+)/$', journal_student, name='journal_student'),
    url(r'^journal/update/$', journal_update, name='journal_update'),
    
    url(r'^exam/$', exam_list, name='exam'),

    url(r'^contact_admin/$', contact_admin, name='contact_admin'),

    # админ панель 
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),

]
#from .settings import MEDIA_ROOT, DEBUG
if DEBUG:
# serve files from media folder этот урл паттерн подключаем только в режиме отладки, 
# на боевом сервере обслуживание медиафалов выполняется напрямую сервером
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        # наши медиафайлы обрабатывает serve из пакета джанго (обработчик статич ресурсов, имя файля в перем path
        # путь к папке  'document_root': MEDIA_ROOT, где MEDIA_ROOT из settings.py
        # чтоб все это работало поле БД для изображ должно хранить имя файла изображения, иначе исключ 
]


