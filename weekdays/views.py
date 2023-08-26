from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def weekdaysuzView(request):
    return HttpResponse('Dushanba, Seshanba, chorshanba, Payshanba, Juma, Shanba, Yakshanba')
def weekdaysenView(request):
    return HttpResponse('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')
def weekdaysruView(request):
    return HttpResponse('Понедельник, вторник, среда, Четверг, Пятница, Суббота, воскресенье')