from django.contrib import admin

from .models import Article, Question


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'subtitle', 'name', 'question']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Question, QuestionAdmin)