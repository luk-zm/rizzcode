from django.shortcuts import render
from .forms import LanguageForm
from .models import Article

def article_list(request):
    form = LanguageForm(request.GET or None)  # Użycie GET, jeśli tak chcesz
    articles = Article.objects.filter()
    selected_language = None

    if form.is_valid():
        selected_language = form.cleaned_data['language']
        articles = Article.objects.filter(language=selected_language)

    return render(request, 'articles.html', {
        'form': form,
        'articles': articles,
        'selected_language': selected_language,
    })
