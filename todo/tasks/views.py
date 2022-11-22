from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Task


def helloWorld(request):
    return HttpResponse('Receive Get!')


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})


def your_name(request, name):
    return render(request, 'tasks/your_name.html', {'name': name})

def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task_view.html', {'task': task})
