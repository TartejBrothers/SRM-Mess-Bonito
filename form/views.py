# form/views.py
from django.shortcuts import render
from .forms import add_data
from .quotes import get_random_quote


def index(request):
    form = add_data(request.POST or None)
    if form.is_valid():
        form.save()
        form = add_data()
        return redirect("success")
    dict5 = {"form": form}
    return render(request, "index.html", dict5)


def success(request):
    quote_text, quote_author = get_random_quote()
    context = {"quote_text": quote_text, "quote_author": quote_author}
    return render(request, "success.html", context)
