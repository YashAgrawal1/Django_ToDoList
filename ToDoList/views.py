from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import PostForm 
from .forms import PostForm , UpdateForm
from django.utils import timezone

# Create your views here.
def task(request):
    data = TaskList.objects.all()
    context = {"data": data}
    return render(request, template_name="ToDoList/home.html", context=context)
    # return HttpResponse('hello world')

def detail(request, id):
    data = TaskList.objects.get(id=id)
    context = {"data": data}
    return render(request,template_name="ToDoList/Detail.html", context=context)

def edit(request, id):
    data = TaskList.objects.get(id=id)
    form = UpdateForm(instance=data )
    if request.method == "POST":
        data = TaskList.objects.get(id=id)
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect(task)
    return render(request, 'ToDoList/Create.html', {'form': form})

def delete(request, id):
    data = TaskList.objects.get(id=id)
    if request.method == "POST":
        data.delete()
        return redirect(task)
    return render(request, 'ToDoList/Delete.html', {'item': data})

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            TaskList = form.save(commit=False)
            TaskList.author = request.user
            TaskList.start_date = timezone.now()
            TaskList.save()
            return redirect(task)
    else:
        form = PostForm()
    return render(request, 'ToDoList/Create.html', {'form': form})





    



    

