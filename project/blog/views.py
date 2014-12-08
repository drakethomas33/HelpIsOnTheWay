from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Question, Article


def home(request):
    context = {"articles": Article.objects.filter(status="published").order_by('published_at').reverse()}
    return render_to_response("index.html", RequestContext(request, context))


def ask(request):
    thank_you = False
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
        thank_you = True
    context = {
        "published_questions": Question.objects.filter(status="published"),
        "thank_you": thank_you
    }
    return render_to_response("ask.html", RequestContext(request, context))