from django.shortcuts import render, redirect
from .models import Task
from .forms import *
# Create your views here.

def home(request):
    tasks = Task.objects.all()

    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
           form.save()
        return redirect("/")

    context = {'form': form}
    return render(request, 'update.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("/")

    context = {'item': task}
    return render(request, 'delete.html', context)