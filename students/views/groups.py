# coding: utf-8
# чтобы с русскими буквами не было проблем, указываем кодировку
from django.shortcuts import render
from django.http import HttpResponse

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
