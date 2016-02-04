# coding: utf-8
# чтобы с русскими буквами не было проблем, указываем кодировку
from django.shortcuts import render
from django.http import HttpResponse
from ..models.students import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# views always  takes on the input  request (object) and always returns HTTPResponse (object) 
# answer rendering template with context 

# вьшки для студентов
def students_list(request):
    list_students = Student.objects.all()
    # здесь мы получаем все объекты модели, все строки таблицы БД, так называемый Queryset
    
    # try to order students list
    reverse = ''
    order_by = request.GET.get('order_by', '')
    if order_by =='':
        order_by = 'last_name'
    # получаем в GET запросе параметр order_by, когда пользователь щелкнет по ссылке 
    #  <a href={% url "home" %}?order_by=last_name>Фамилия&uarr;</a> 
    # GET вернет нам в order_by - last_name or first_name or ticket
    # параметр запроса сразу за знаком ?
    # если пользователь не щелкал по ссылке, то order_by - пустой, и мы присваиваем ему значение 'last_name'
    # это мы устанавливаем сотрировку вывода по умолчанию по этому полю
    
    if order_by in ('last_name', 'first_name', 'ticket'):
        # если щелкнули имя, фамилия или билет
        list_students = list_students.order_by(order_by)
        # сортируем наш список по этому полю по возрастанию, сортируем сам Queryset, 
        # то что получили при запросе к классу модели
        if request.GET.get('reverse', '') == '1':
            list_students = list_students.reverse()

    # paginate students
    paginator = Paginator(list_students, 3)
    # пагинатор объкт класса, который содержит список студентов группированный по три
    # у него есть атрибут page который нам даст студентов соответствующих номеру страницы из звпроса
    # также он знает сколько у него страниц и генерирует исключения при ошибке номера страницы
    page = request.GET.get('page')
    try:
        list_students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_students = paginator.page(1)
        # если не смогли выичслить номер страницы - поазываем первую
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        list_students = paginator.page(paginator.num_pages)
        # если выичислили но больше чем у нас есть, показываем последнюю
    
    return render(request, 'students/students_list.html', {'students': list_students, 'order_by_1': order_by, 'reverse_1':reverse})
    # return render(request,'students/students_list.html', {'students': list_students})
    # добавили третий аргумент - словарь с ключом  list_students = списку студентов, по этому ключу получаем доступ 
    # к списку студентов, этот словарь - контекст шаблона, через который данные из вьюшки передаются в шаблон
    # в шаблоне по ключу students получаем доступ к списку студентов, список студентов берем из БД такой вот штукой
    # Student.objects.all() кроме списка студентов передаем две переменные order_by_1 и reverse_1 - это начальные 
    # установки для вывода данных в отсортированном виде сразу при загрузки 
    # после применения пагинатора наш список студентов - это уже набор страниц, который будет выводится - 
    # сразу после загрузки - первая страница, затем по кликанью на пагинаторе - выводим тех студентов, которые 
    # соответствуют номеру страницы . Номер страницы - переменная  page - значение поступает в GET из ШТМЛ шаблона


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
