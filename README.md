# students
Система учета студентов (переработанная версия) с Виталием Подоба


Вопрос
contact_admin.py
form.html

Во вьшке contact_admin.py работаю с messages
Message по ошибке заполнения данных не отрабатывает, сделала статическое сообщение  в form.html
при этом и там и там я пользуюсь form.errors


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

