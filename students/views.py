# coding: utf-8
# чтобы с русскими буквами не было проблем, указываем кодировку
from django.shortcuts import render
from django.http import HttpResponse

# views always  takes on the input  request (object) and always returns HTTPResponse (object) 
# answer rendering template with context 

# вьшки для студентов
def students_list(request):
    list_students = (
        {'id': 1,
        'first_name': u'Наталья',
        'last_name': u'Куличик',
        'ticket': 235,
        'image': 'img/keks.jpg'},
        {'id': 2,
        'first_name': u'Андрей',
        'last_name': u'Корост',
        'ticket': 2123,
        'image': 'img/cat_acrobat.png'},
        {'id': 3,
        'first_name': u'Анна',
        'last_name': u'Иванова',
        'ticket': 2345,
        'image': 'img/cat_eyes.png'},
    )
    # добавили переменную list_students = кортежу из трех элементов, каждый элемент кортежа словарь 

    return render(request,'students/students_list.html', {'students': list_students})
    # добавили третий аргумент - словарь с ключом  list_students = списку студентов, по этому ключу получаем доступ 
    # к списку студентов, этот словарь - контекст шаблона, через который данные из вьюшки передаются в шаблон
    # в шаблоне по ключу students получаем доступ к списку студентов
# Create your views here. I created

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)
# sid  - идентификатор студента, передаются из вебадреса страницы на наш урл паттерн, 
# который нам его ловит и передает во вьюшку
# в 21 строке используется %s - оператор форматирования, который перем sid приводит к строковому типу, 
# чтобы сформировать заголовок страницы с содержанием id студента

#вьюшки для групп
def groups_list(request):

    list_groups = (
        {'id': 1,
        'name': u'M21-2',
        'leader': {'id': 1, 'name': u'Куличик'}},
        {'id': 2,
        'name': u'M21-3',
        'leader': {'id': 2, 'name': u'Иванов'}},
        {'id': 3,
        'name': u'M21-1',
        'leader': {'id': 3, 'name': u'Петров'}},
    )
# моделируем наличие базы данных

    return render(request,'students/groups_list.html', {'groups': list_groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)

#вьюшки для журналов
def journal_list(request):
	return render(request, 'students/journal_list.html')

def journal_student(request, sid):
	return HttpResponse('<h1>students journal %s</h1>' % sid)

def journal_update(request):
	return HttpResponse('<h1> udate journal </h1>')

