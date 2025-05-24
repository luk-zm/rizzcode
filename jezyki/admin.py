from django.contrib import admin

# Register your models here.

from .models import Article, Language


class ArticleAdmin(admin.ModelAdmin):
    # dodac fieldset
    fields = ["title", "content",
              "link", "language",]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Language)
