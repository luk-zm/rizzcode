from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm  

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('exercise-list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login/login.html'
