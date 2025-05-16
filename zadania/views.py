from django.shortcuts import render, get_object_or_404
from .models import Exercise

def zadania(request):
    exercises = Exercise.objects.all()
    return render(request, "zadania/exercise_list.html", {"exercises": exercises})

def zadania_po_jezyku(request, lang):
    lang_map = {
        "python": "Py",
        "sql": "SQL",
        "csharp": "C#",
    }
    lang_code = lang_map.get(lang.lower())
    exercises = Exercise.objects.filter(language=lang_code) if lang_code else Exercise.objects.none()
    return render(request, "zadania/exercise_list.html", {
        "exercises": exercises,
        "selected_language": lang.capitalize()
    })

def szczegoly_zadania(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    return render(request, "zadania/exercise_detail.html", {"exercise": exercise})
