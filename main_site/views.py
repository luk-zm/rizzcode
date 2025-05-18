from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import LanguageForm
from .models import Article
from .forms import CustomUserCreationForm  

def article_list(request):
    form = LanguageForm(request.GET or None)  # Użycie GET, jeśli tak chcesz
    articles = Article.objects.filter()
    selected_language = None

    if form.is_valid():
        selected_language = form.cleaned_data['language']
        articles = Article.objects.filter(language=selected_language)

    return render(request, 'main_site/articles.html', {
        'form': form,
        'articles': articles,
        'selected_language': selected_language,
    })


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


def index(request):
    return render(request, 'main_site/index.html')
