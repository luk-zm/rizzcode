from django.contrib.auth.models import User


from django.db import models

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_lenght=1000)
   
    class Rating(models.Integer):
        SHIT = 1
        BAD = 2
        OKAY = 3
        GOOD = 4
        RIZZ = 5
    rating = models.IntegerField(choices=Rating)


class Exercise(models.Model):
    user = models.OnetoOneField(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    solution = models.CharField(max_lenght=10000)

