import json

import mailchimp

from django.http import HttpResponse
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


def subscribe(request):
    # This will subscribe this person with MailChimp.
    # Note double_optin=False means the user will be subscribed immediately,
    # rather than MailChimp emailing them an explicit opt in email.
    # See http://kb.mailchimp.com/lists/signup-forms/the-double-opt-in-process
    m = mailchimp.Mailchimp('22d12387b2447552b61abd6dc2b441e1-us9')
    try:
        m.lists.subscribe('708c29a51b', {'email': json.loads(request.body)['email']}, double_optin=False)
        return HttpResponse()
    except mailchimp.Error as e:
        return HttpResponse(str(e), status=400)


class ArticleDetail(DetailView):
    template_name = 'article_detail.html'
    model = Article


class QuestionDetail(DetailView):
    template_name = 'question_detail.html'
    model = Question