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
    # добавили переменную list_students = кортежу из трех элементов, каждый элемент кортежа словарь, имитация бд

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
