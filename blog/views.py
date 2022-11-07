from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'blog/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'blog/about.html')

def create(request):
    error =''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            error = "Форма не верная"
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create.html', context)
