from typing import Any, Dict
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'success': 'Inscirption réussi avec succès'}) 
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'error': error_message})
        
    return render(request, 'register.html')

def login_view(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html', {'error': 'Email ou mot de passe incorrect'})
    
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name, 'email': request.user.email, 'last_name': request.user.last_name})

@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.first_name + " " + request.user.last_name })


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required
def joinroom(request):
    if request.method=='POST':
        roomId = request.POST['roomID']
        return redirect('/meeting?roomID='+roomId)
    return render(request, 'joinroom.html', {'name': request.user.first_name + " " + request.user.last_name })

@login_required
def profile(request):
    return render(request, 'profile.html', {'name': request.user.first_name + " " + request.user.last_name })

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
            
            context['search_input'] = search_input
        return context
    
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'video_app/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
        
class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


