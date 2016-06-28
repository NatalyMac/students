# coding: utf-8
# чтобы с русскими буквами не было проблем, указываем кодировку
from django.shortcuts import render
from django.http import HttpResponse
#вьюшки для журналов
def journal_list(request):
	return render(request, 'students/journal_list.html')

def journal_student(request, sid):
	return HttpResponse('<h1>students journal %s</h1>' % sid)

def journal_update(request):
	return HttpResponse('<h1> udate journal </h1>')