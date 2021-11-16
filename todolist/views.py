from django.shortcuts import render, redirect
from .models import TaskList
from django.contrib import messages
from .forms import TaskForm
from django.core.paginator import Paginator

def homepage(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('New Task Added!'))
        return redirect('home')
    else:
        task = TaskList.objects.all()
        paginator = Paginator(task, 5)
        page = request.GET.get('pg')
        task = paginator.get_page(page)
        context = {'form': task}
        return render(request, 'homepage.html', context)

def delete(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('home')

def edit(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ('Task Edited!'))
        return redirect('home')
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'edit.html', context)

def task(request, task_id):
    tasks = TaskList.objects.get(pk=task_id)
    if tasks.done:
        tasks.done = False
        tasks.save()
    else:
        tasks.done = True
        tasks.save()
    return redirect('home')

def contact(request):
    context = {'welcome_text': 'Welcome to Contact page'}
    return render(request, 'contact.html', context)

def about(request):
    context = {'welcome_text': 'Welcome to About page'}
    return render(request, 'about.html', context)

def index(request):
    context = {'index': 'Welcome to the Index Page'}
    return render(request, 'index.html', context)