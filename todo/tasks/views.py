from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def helloWorld(request):
    if request.method == 'GET':
        return HttpResponse('Receive Get!')


def task_list(request):
    return render(request, 'tasks/list.html')


def your_name(request, name):
    return render(request, 'tasks/your_name.html', {'name': name})
