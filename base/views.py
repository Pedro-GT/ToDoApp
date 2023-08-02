from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
# Create your views here.

def home(request):
    form = TaskForm(request.POST or None)  
    tasks = Task.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, " Task added ")
            return redirect('home')    
    else:
        return render(request, "home.html", {'tasks':tasks, 'form':form })

def delete_task(request,pk):
    task = Task.objects.get(id = pk)
    task.delete()
    messages.success(request, " Task concluded ")
    return redirect('home')
    
        
    
    
