# coding: utf-8
# чтобы с русскими буквами не было проблем, указываем кодировку
from django.shortcuts import render
from django.http import HttpResponse
from ..models.exams import Exam
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# views always  takes on the input  request (object) and always returns HTTPResponse (object) 
# answer rendering template with context 

# вьшки для экзаменов
def exam_list(request):
    list_exams = Exam.objects.all()
    return render(request,'students/exam_list.html', {'exams': list_exams})

# пока просто выводим список, дальше надо подумать о красотах

    
