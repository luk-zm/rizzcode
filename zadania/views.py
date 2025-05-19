from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise, Solution
from .forms import SolutionUploadForm, SQLSolutionForm
from django.contrib.auth.decorators import login_required
import subprocess
from django.utils import timezone
from django.db.models import Count
from django.db import connection
import re

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

@login_required
def submit_solution(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)

    if request.method == 'POST':
        print("Form was submitted")
        form = SolutionUploadForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.exercise = exercise
            solution.user = request.user
            solution.pub_date = timezone.now()
            solution.save()

            # tu możesz odczytać i sprawdzić zawartość pliku solution.code_file.path

            return redirect('upload-solution', exercise_id=exercise.id)
    else:
        form = SolutionUploadForm()

    return render(request, 'zadania/submit_solution.html', {'exercise': exercise, 'form': form})

@login_required
def upload_solution(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)

    if request.method == 'POST':
        print("Form was uploaded")
        form = SolutionUploadForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.user = request.user
            solution.exercise = exercise
            solution.pub_date = timezone.now()
            solution.save()

            file_path = solution.code_file.path

            try:
                result = subprocess.run(
                    ['python', file_path],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output = result.stdout
                output_clean = ''.join(output.split())
                expected_clean = ''.join(exercise.assert_output.split())

                if output_clean == expected_clean:
                    solution.completed = True
                    solution.save()
                    return render(request, 'zadania/success.html', {'exercise': exercise})
                else:
                    return render(request, 'zadania/failure.html', {'exercise': exercise, 'output': output})

            except subprocess.TimeoutExpired:
                output = 'Execution timeout'
                return render(request, 'zadania/failure.html', {'exercise': exercise, 'output': output})

    else:
        form = SolutionUploadForm()

    return render(request, 'zadania/upload_solution.html', {'exercise': exercise, 'form': form})

def szczegoly_zadania(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    
    user_solutions = Solution.objects.filter(exercise=exercise, user=request.user)
    
    attempts = user_solutions.count()  # ile wysłał rozwiązań
    successes = user_solutions.filter(completed=True).count()  # ile razy było poprawne
    last_attempt = user_solutions.order_by('-pub_date').first()  # ostatnie rozwiązanie
    
    context = {
        'exercise': exercise,
        'attempts': attempts,
        'successes': successes,
        'last_attempt': last_attempt,
    }
    return render(request, 'zadania/exercise_detail.html', context)

@login_required
def submit_sql_solution(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    error_message = None

    if request.method == 'POST':
        form = SQLSolutionForm(request.POST)
        if form.is_valid():
            user_query = form.cleaned_data['solution_text'].strip()

            def normalize_sql(sql):
                sql = sql.lower()
                sql = re.sub(r'\s+', ' ', sql)
                return sql.strip()

            user_sql_normalized = normalize_sql(user_query)
            expected_sql_normalized = normalize_sql(exercise.assert_output)

            solution = Solution.objects.create(
                user=request.user,
                exercise=exercise,
                solution_text=user_query,
                pub_date=timezone.now(),
                completed=user_sql_normalized == expected_sql_normalized
            )

            if solution.completed:
                return render(request, 'zadania/success.html', {'exercise': exercise})
            else:
                return render(request, 'zadania/failure1.html', {
                    'exercise': exercise,
                    'user_sql': user_query,
                    'expected_sql': exercise.assert_output
            })
        else:
            error_message = "Invalid form submission."
    else:
        form = SQLSolutionForm()

    return render(request, 'zadania/submit_sql_solution.html', {
        'exercise': exercise,
        'form': form,
        'error_message': error_message,
    })