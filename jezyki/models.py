from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=32)

    def __str__(self):
        return self.language

class Article(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    link = models.URLField(blank=True)  
    language = models.ForeignKey(Language, related_name='articles', on_delete=models.CASCADE)

