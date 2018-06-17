from django.shortcuts import render
from django.http import HttpResponse

def get_ip(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip="notDefined"
    return ip

def index (request):
    print(get_ip(request))
    return HttpResponse("<h3>Привет мир</h3>")
