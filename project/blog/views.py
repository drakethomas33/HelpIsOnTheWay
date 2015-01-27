from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView

from .models import Question, Article


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')
        if not name or not email or not question:
            pass
        Question.objects.create(
            name=name,
            email=email,
            question=question,
        )
    context = {
        "articles": Article.objects.filter(status="published").order_by('published_at').reverse(),
        "published_questions": Question.objects.filter(status="published"),
        "thank_you": request.method == "POST"
    }
    return render_to_response("index.html", RequestContext(request, context))


def ask(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')
        if not name or not email or not question:
            pass
        Question.objects.create(
            name=name,
            email=email,
            question=question,
        )
    context = {
        "published_questions": Question.objects.filter(status="published"),
        "thank_you": request.method == "POST"
    }
    return render_to_response("ask.html", RequestContext(request, context))


class ArticleDetail(DetailView):
    template_name = 'article_detail.html'
    model = Article


class QuestionDetail(DetailView):
    template_name = 'question_detail.html'
    model = Question