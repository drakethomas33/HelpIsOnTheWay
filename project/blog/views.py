def ask(request):
    if request.method == "POST":
        print request.POST
    c = RequestContext(request, {})
    return render_to_response("ask.html", c)