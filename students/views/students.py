# coding: utf-8
# чтобы с русскими буквами не было проблем, указываем кодировку
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.students import Student
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import messages
from django.views.generic import UpdateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm


# views always  takes on the input  request (object) and always returns HTTPResponse (object) 
# answer rendering template with context 


# вьшки для студентов
def students_list(request):
    list_students = Student.objects.all()
    # здесь мы получаем все объекты модели, все строки таблицы БД, так называемый Queryset
    
    # try to order students list
    order_by_default = '0'
    # инициализация переменной, и дальше не мешает
    order_by = request.GET.get('order_by', '')
    # второй параметр передача значения по умолчанию, но нас такая передача не устраивает, 
    # теряем значение по умолчанию для корректного изображения в шаблоне
    if order_by =='':
        order_by = 'last_name'
        order_by_default = '1'
        
    # получаем в GET запросе параметр order_by, когда пользователь щелкнет по ссылке 
    #  <a href={% url "home" %}?order_by=last_name>Фамилия&uarr;</a> 
    # GET вернет нам в order_by - last_name or first_name or ticket
    # параметр запроса сразу за знаком ?
    # если пользователь не щелкал по ссылке, то order_by - пустой, и мы присваиваем ему значение 'last_name'
    # это мы устанавливаем сортировку вывода по умолчанию по этому полю и ввводим переменную, которая помнит
    # режим по умолчанию, пока пользователь не щелкнет ссылку
    # перем по умолч нужна, чтобы нарисовать стрелочку и исключить двой вывод сортировку по возрастанию
    # если не сделать, то таблица выводится сортированная по возрастанию, но щелчок по ссылке приводит 
    # не к изменению направления сортировки, а к повторному выводу сортировки по возрас
    
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
    
    return render(request, 'students/students_list.html', {'students': list_students, 'order_by_default':order_by_default})
    # 'reverse_1':reverse
    # return render(request,'students/students_list.html', {'students': list_students})
    # добавили третий аргумент - словарь с ключом  list_students = списку студентов, по этому ключу получаем доступ 
    # к списку студентов. этот словарь - контекст шаблона, через который данные из вьюшки передаются в шаблон.
    # в шаблоне по ключу students получаем доступ к списку студентов, список студентов берем из БД такой вот штукой
    # Student.objects.all(). кроме списка студентов передаем две переменные order_by_1 и reverse_1 - это начальные 
    # установки для вывода данных в отсортированном виде сразу при загрузке
    # после применения пагинатора наш список студентов - это уже набор страниц, который будет выводится - 
    # сразу после загрузки - первая страница, затем по кликанью на пагинаторе - выводим тех студентов, которые 
    # соответствуют номеру страницы . Номер страницы - переменная  page - значение поступает в GET из ШТМЛ шаблона


def students_add(request):

# Если форма была отправлена:
   # Проверяем была ли нажата кнопка Отменить после отправки формы Если да:
     # Возвращаем пользователя к списку студентов 
  # Если кнорка Добавить была нажата:
     # Проверяем данные на корректность и собираем ошибки
     # Если данные введены некорректно:
         # Отдаем шаблон формы вместе с найденными ошибками
     # Если данные введены корректно:
          # Создаем и сохраняем студента в базу
          # Повертаємо користувача до списку студентів
# Если форма не была отправлена:
   # возвращаем код начального состояния формы

# was form posted?
    request.session['student_added'] = ''
    # обнуляем данные о студенте перед заполнением формы
    if request.method == "POST":
# was form add button clicked?
        if request.POST.get('add_button'):

    # TODO: validate input from user
            errors = {}
            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),'notes': request.POST.get('notes')}
            # validate user input
            
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Имя обязательное поле"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Фамилия обязательное поле"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата рождения обязательное поле"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введите корректный формат даты (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер билета обязательное поле"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Выберите группу"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Выберите корректный номер группы"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            
            if not errors:
        # create student object
                student = Student(**data)
                # save it to database
                student.save()
                # redirect user to students list
                request.session['student_added'] = student.last_name+' '+student.first_name
                #request.session['student_addedFN'] = student.first_name
                # сохраняю в словаре сессии добавленного студента
                messages.success(request, 'Студент успешно добавлен!')
                # сформировали сообщение статуса, которое будет отображаться на страницу редиректа
                # виды  success, debug, warning, info, error
                # return HttpResponseRedirect(u'%s?status_message=Студент успешно добавлен!'%reverse('home'))
                return HttpResponseRedirect(reverse('home'))
            else:
            # render form with errors and previous user input
                return render(request, 'students/students_add.html',{'groups': Group.objects.all().order_by('title'),\
                'errors': errors})
             # надо попробоваь написать обработчик для сообщений статуса, и привязать к базовому шаблону
        elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
            request.session['student_added'] = ''
            messages.warning(request, 'Добавление студента отменено!')
            #обнуляем данные о студенте, если кансел
            #return HttpResponseRedirect(u'%s?status_message=Добавление студента отменено!'%reverse('home'))
            return HttpResponseRedirect(reverse('home'))
    else:
    # initial form render
        return render(request, 'students/students_add.html',{'groups': Group.objects.all().order_by('title')})

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # указание полей обязательно
   
    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        # set form tag attributes
        self.helper.form_action = reverse('students_edit',
        kwargs={'pk': kwargs['instance'].id})

        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(Submit('add_button', u'Сохранить', css_class="btn btn-primary"),\
            Submit('cancel_button', u'Отменить', css_class="btn btn-warning"),)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'students/students_edit.html'
    #fields = '__all__'
    # указание полей обязательно для формы, иначе ошибка - без полей использ класса запрещено
    # можно указать только те поля, которые нужны, или все
    # если есть атрибут form_class - то поля в этом классе не указываем, но в классе ModelForm обязательно
    success_url = reverse_lazy('home')
    # или атрибут или метод для определения урла редиректа в случае успешного исхода
    # используем lazy - определяет урл до загрузки файла урлов, просто reverse - ошибка 
    # def get_success_url(self):
        # return reverse('home')
        # у подобы отсутствует название функции для этой строки
        # насколько я поняла здесь мы определяем адрес возврата при успешном выполнении операции 
        # записи в базу, то ж самое можно сделать прямо в урлах

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button') is not None:
            # здесь тоже не хватает в коде , без is not None не работает
            messages.warning(request, "Редактирование отменено!")
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, "Редактирование прошло успешно!")
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

#def students_edit(request, sid):
#return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
   return HttpResponse('<h1>Delete Student %s</h1>' % sid)
# sid  - идентификатор студента, передаются из вебадреса страницы на наш урл паттерн, 
# который нам его ловит и передает во вьюшку
# в 21 строке используется %s - оператор форматирования, который перем sid приводит к строковому типу, 
# чтобы сформировать заголовок страницы с содержанием id студента