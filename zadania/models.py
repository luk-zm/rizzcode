from django.conf import settings

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Exercise(models.Model):
    class LanguageChoices(models.TextChoices):
        CSHARP = "C#", "Csharp"
        PYTHON = "Py", "Python"
        SQL = "SQL", "Structured Query Language (SQL)"

    title = models.CharField(
        max_length=30,
        help_text="Title of the exercise."
    )

    instruction = models.CharField(
        max_length=300,
        help_text="The instruction to be displayed."
    )

    assert_output = models.CharField(
        max_length=1000,
        help_text="Output (code) to be asserted."
    )

    language = models.CharField(
        max_length=10,
        choices=LanguageChoices.choices,
        default=LanguageChoices.PYTHON,
        help_text="Programming language of the exercise."
    )


    def __str__(self):
        return self.title



class Solution(models.Model):
    """
    Published exercise. 1:1 to the Test model.
    """
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    # wypierdolić — to nawet nie korzysta z bazy danych...
    code_file = models.FileField(upload_to='solutions/', null=True, blank=True)
    solution_text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField("Date Added")

    def __str__(self):
        return f'Solution by {self.user.username} for {self.exercise.title}'


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)

    class Meta:
        ordering = ['-pub_date']

    class Rating(models.IntegerChoices):
        SHIT = 1
        BAD = 2
        OKAY = 3
        GOOD = 4
        RIZZ = 5
    rating = models.IntegerField(choices=Rating)
    pub_date = models.DateTimeField(auto_now_add=True)
    # UPDATE TIMEZONE!!!

    def get_comment(self) -> str:
        return f"{self.user.username}({self.rating}):{self.comment[:20]}"

    def __str__(self):
        return self.get_comment()
