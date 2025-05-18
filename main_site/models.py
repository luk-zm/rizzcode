from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Language(models.Model):
    language = models.CharField(max_length=255)

    def __str__(self):
        return self.language


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    link = models.URLField(blank=True)  
    language = models.ForeignKey(Language, related_name='articles', on_delete=models.CASCADE)



class Exercise(models.Model):
    title = models.CharField(max_length=30,
                             help_text="Title of the exercise.")
    instruction = models.CharField(max_length=300,
                                   help_text="The Instruction to be displayed."

                                   )
    assert_output = models.CharField(max_length=1000,
                                     help_text="Output (code) to be asserted.")
    languages = {
        "C#": "Csharp",
        "Py": "Python",
        "SQL": "Structured Query Language (SQL)"
    }
    # define langs as a choice

    def __str__(self):
        return self.assert_output


class Solution(models.Model):
    """
    Published exercise. 1:1 to the Test model.
    """
    test = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    solution = models.CharField(max_length=5000)
    pub_date = models.DateTimeField("Date Added")


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
