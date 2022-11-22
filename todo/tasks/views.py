from django.shortcuts import render
from django.http import HttpResponse

from .models import Task


def helloWorld(request):
    return HttpResponse('Receive Get!')


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})


def your_name(request, name):
    return render(request, 'tasks/your_name.html', {'name': name})
