# coding: utf-8
# чтобы с русскими буквами не было проблем, указываем кодировку
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib import messages
from django import forms
from django.core.mail import send_mail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from studentsdb.settings import ADMIN_EMAIL

class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label=u"Ваш e-mail")

    subject = forms.CharField(
        label=u"Тема письма",
        max_length=128)

    message = forms.CharField(
        label=u"Текст письма",
        max_length=2560,
        widget=forms.Textarea)
    # по умолчанию все поля формы обязательные для заполнения

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Отправить'))

# views always  takes on the input  request (object) and always returns HTTPResponse (object) 
# answer rendering template with context 

def contact_admin(request):
    #return HttpResponse('привет')
    #return render(request, 'contact_admin/form.html', {})
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

        # Этот коммент для кода Подобы где он шлет напрямую статусные сообщения в HTTPResponse
        # у Поlобы здесь ошибка - переменная для сообщения не инициализирована, она примет значения, 
        # только если данные валидны, а ответ форма должна вернуть в любом случае - HTTPResponse должен вернуть данные
        # иначе ошибка
        # Поэтому я присвоила пустое значение переменной messages, которая вернет статусное сообщение
        # check whether user data is valid:
        if form.is_valid():
            # send email
            subject = form.cleaned_data['subject'] + '     (' +  form.cleaned_data['from_email'] + ')'
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
        
            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                messages.warning(request, 'Во время отправки возникла ошибка, попробуйте позже')
            else:
                request.session['student_added'] = '' 
                #  редко возникающая проблема - при сообщении об успешном отправлении письма, выводится имя 
                #  последнего добавленного студента. Нужно понаблюдать
                messages.success(request, 'Письмо успешно отправлено!')

        # redirect to the same contact page with success message
        else:
            if form.errors:
                form = ContactForm(form.cleaned_data)
                # !!!!! Вот здесь засада, было
                # messages.error = (request, 'Исправьте ошибки, пожалуйста')
                # но не захотела работать, сделала для ошибок в form.html статич запись
                # Почему? подобные сообщения об  успехе или временной недоступности доступны в form.html
                # и прекрасно выводятся, а это сообщение нет
                # 

                return render(request, 'contact_admin/form.html', {'form': form})
        
        return HttpResponseRedirect(reverse('contact_admin'))
        
        
        # if there was not POST render blank form
    else:
        form = ContactForm()
        return render(request, 'contact_admin/form.html', {'form': form})
    

















