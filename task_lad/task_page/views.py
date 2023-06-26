from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Task
import datetime
from .forms import UserRegisterForm, UserUpdateForm, TaskCreationForm, TaskUpdateForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone


# task modifications
def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk = request.user.id )
        tasks = user.task_set.filter(Q(completion = False)).order_by('deadline')[:5]
        tasks_number = tasks.count()

        context = {
            'tasks': tasks,
            'tasks_number': tasks_number
        }
        return render(request, 'task_page/index.html', context)
    else: 
        context = {}
        return render(request, 'task_page/index.html', context)
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            messages = ["the user does not exist"]
            context = {
                'messages': messages
            }
            return render(request, 'task_page/index.html', context)

        else:
            user = authenticate(request, username= username, password=password) 
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('task_page:index'))
            else:
                messages = ["username or password incorrect"]
                context = {
                'messages': messages
                }
                return render(request, 'task_page/index.html', context)
    context = {}
    return render(request, 'task_page/login_user.html', context)


@login_required(login_url='task_page:index')
def logout_user(request):
    logout(request)
    return redirect('task_page:index')


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_page:index')
        else:
            messages.error(request, 'something went wrong on the registration, try again')
    form = UserRegisterForm()
    context = {
        'form': form
        }
    return render(request, 'task_page/register_user.html', context)
    

@login_required(login_url='task_page:index')
def update_user(request):
    if request.method == 'POST':
            form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('task_page:index')
            else:
                messages.error(request, "something went wrong on the user update")
    form =  UserUpdateForm(instance=request.user)
    context = {
        'form': form
    }   
    return render(request, 'task_page/update_user.html', context)


@login_required(login_url='task_page:index')
def task_creation(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            if task.deadline >= timezone.now():  
                task.save()
                return redirect('task_page:index')
            else:
                messages.error(request, 'please set a greater deadline than the current datetime')
        else:
            messages.error(request, 'something went wrong during the task creation')
    form = TaskCreationForm()
    context = {
        'form': form
    }
    return render(request, 'task_page/task_creation.html', context)


@login_required(login_url='task_page:index')
def task_completion(request, id):
    task = get_object_or_404(Task, pk=id)
    task.completion = True
    task.completed = timezone.now()
    if task.completed > task.deadline:
        task.delay = True
    else:
        task.delay = False    
    task.save()
    return redirect("task_page:index")


@login_required(login_url='task_page:index')
def task_update(request, id):
    task = get_object_or_404(Task, pk=id)
    q = request.GET.get('q')
    if q == None:
        if request.method == 'POST':
            form = TaskUpdateForm(request.POST,instance=task)
            if form.is_valid():
                task = form.save(commit=False)
                if task.deadline >= timezone.now():  
                    task.save()
                    return redirect('task_page:index')
                else:
                    messages.error(request, 'please set a greater deadline than the current datetime')
            else:
                messages.error(request, 'something went wrong during task update')
        form = TaskUpdateForm(instance=task)
    else:
        task.deadline = timezone.now()
        task.completion = False
        task.delay = False
        task.save()
        form = TaskUpdateForm(instance=task)  
    context = {
        'form': form,
        'id': id
    }
    return render(request, 'task_page/task_update.html', context)


@login_required(login_url='task_page:index')
def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('task_page:index')


@login_required(login_url='task_page:index')
def user_profile(request):
    user = request.user
    q = request.GET.get('q') if request.GET.get('q') != None else 'tasks'
    filters = {
        'tasks': user.task_set.all(),
        'completed tasks': user.task_set.filter(completion = True),
        'uncompleted tasks': user.task_set.filter(completion = False),
        'delayed tasks': user.task_set.filter(delay = True),
        'in time tasks': user.task_set.filter(delay = False),
        'uncompleted delayed tasks': user.task_set.filter(Q(delay = True) & Q(completion=False)),
        'completed delayed tasks': user.task_set.filter(Q(delay = True) & Q(completion=True)),
        'completed in time tasks': user.task_set.filter(Q(delay = False) & Q(completion=True)),
        'uncompleted in time tasks': user.task_set.filter(Q(delay = False) & Q(completion=False)),    
    }
    tasks = filters[q]
    tasks_count = tasks.count()
    context = {
        'filters': filters,
        'tasks': tasks,
        'tasks_count': tasks_count,
        'q': q
                }
    return render(request, 'task_page/user_profile.html', context)    


@login_required(login_url='task_page:index')
def task_completed(request, id):
    task = get_object_or_404(Task, pk=id)
    context = {
        'task': task
        }
    return render(request, 'task_page/task_completed.html', context)
