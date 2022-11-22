from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task
from django.contrib import messages
from django.core.paginator import Paginator



def helloWorld(request):
    return HttpResponse('Receive Get!')

def task_list(request):
    tasks_list = Task.objects.all().order_by('-created_at')

    paginator = Paginator(tasks_list, 3)

    page = request.GET.get('page')

    tasks = paginator.get_page(page)

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
            messages.info(request, 'Tarefa adicionada com sucesso')
            new_task.save()
            #Return to home
            return redirect('/')
    
    else:
        form = TaskForm()
        return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request, id):
    # Buscar a task
    task = get_object_or_404(Task, pk=id)
    #Prepoular o formulario para edicao, utiliza a instancia
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            #Salva alteracao
            form.save()
            messages.info(request, 'Tarefa editada com sucesso')
            return redirect('/')
        else:
            return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def delete_task(request, id):
    # Buscar a task
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso')
    return redirect('/')
