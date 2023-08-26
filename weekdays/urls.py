from .views import weekdaysuzView, weekdaysruView, weekdaysenView
from django.urls import path

urlpatterns = [
    path('weekdays/uz', weekdaysuzView, name='weekdays'),
    path('weekdays/en', weekdaysenView, name='weekdays1'),
    path('weekdays/ru', weekdaysruView, name='weekdays2')
]