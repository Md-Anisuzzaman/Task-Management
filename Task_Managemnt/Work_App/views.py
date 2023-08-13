from django.shortcuts import render, redirect
from django.urls import reverse
from Work_App.models import TaskModel
from Work_App.forms import TaskForm


def home(request):
    return render(request, 'base.html')


def create_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save(commit=True)
            return redirect('showtaskpage')
    else:
        task = TaskForm()

    return render(request, 'createTask.html', {'task': task})


def show_task(request):
    allTask = TaskModel.objects.all()
    return render(request, 'show_task.html', {'allTasks': allTask})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        datas = TaskForm(request.POST, instance=task)
        if datas.is_valid():
            datas.save()
            return redirect('/show/')
    return render(request, 'edit_task.html', {'form': form})


def complete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('/completed/')


def completed_task_lists(request):
    allTasks = TaskModel.objects.all()
    return render(request, 'completed_tasks.html', {'allTasks': allTasks})


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('/show/')
