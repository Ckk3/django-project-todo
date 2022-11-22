from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task



def helloWorld(request):
    return HttpResponse('Receive Get!')

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})

def your_name(request, name):
    return render(request, 'tasks/your_name.html', {'name': name})

def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task_view.html', {'task': task})

def new_task(request):
    if request.method == 'POST':
        #Verifica se o metodo e post, ou seja, os dados ja vieram do request
        form = TaskForm(request.POST)

        if form.is_valid():
            #Cria a task porem nao salva ainda
            new_task = form.save(commit=False)
            # Add doing equal doing
            new_task.done = '1'
            new_task.save()
            #Return to home
            return redirect('/')
    
    else:
        form = TaskForm()
        return render(request, 'tasks/add_task.html', {'form': form})
