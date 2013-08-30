#Clean template rendering code
from django.shortcuts import render
import datetime

def new_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
