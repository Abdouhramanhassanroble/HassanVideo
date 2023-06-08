from django.shortcuts import render, redirect
from .forms import RegisterForm, EditUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return render(request, 'profile.html', {'success': 'Profil mis à jour avec succès'}) 
        else:
            error_message = form.errors.as_text()
            return render(request, 'editprofile.html', {'error': error_message})
        
    form = EditUserForm(instance=request.user)
    return render(request, 'editprofile.html', {'form': form})



