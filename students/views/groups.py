# coding: utf-8
# чтобы с русскими буквами не было проблем, указываем кодировку
from django.shortcuts import render
from django.http import HttpResponse
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#вьюшки для групп
def groups_list(request):

    """list_groups = (
        {'id': 1,
        'name': u'M21-2',
        'leader': {'id': 1, 'name': u'Куличик'}},
        {'id': 2,
        'name': u'M21-3',
        'leader': {'id': 2, 'name': u'Иванов'}},
        {'id': 3,
        'name': u'M21-1',
        'leader': {'id': 3, 'name': u'Петров'}},
    )"""
# моделируем наличие базы данных
    list_groups = Group.objects.all()
    reverse = ''
    order_by = request.GET.get('order_by', '')
    if order_by =='':
        order_by = 'title'

    if order_by == 'title':
        list_groups = list_groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            list_groups = list_groups.reverse()

    paginator = Paginator(list_groups, 3)
    page = request.GET.get('page')
    try:
        list_groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_groups = paginator.page(1)
        # если не смогли выичслить номер страницы - поазываем первую
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        list_groups = paginator.page(paginator.num_pages)
        # если выичислили но больше чем у нас есть, показываем последнюю
    
    return render(request,'students/groups_list.html', {'groups': list_groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
