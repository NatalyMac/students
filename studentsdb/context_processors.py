# coding: utf-8

#from .settings import PORTAL_URL

def students_proc(request):
    my_portal_url = 'http://' + request.get_host()
    # из request получаем имя хоста, добавляем префикс http и возвращаем в шаблон
    return {'PORTAL_URL': my_portal_url}
    #return {'PORTAL_URL': PORTAL_URL}