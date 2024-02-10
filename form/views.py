# form/views.py
from django.shortcuts import render, redirect
from .forms import add_data
from .quotes import get_random_quote
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Details

from datetime import datetime

day = datetime.now().weekday()

menu = [
    [
        "Breakfast",
        [
            "Roti",
            "Tea",
            "Coffee",
        ],
        "Lunch",
        ["Dal", "Rice", "Chapati", "Sabji"],
        "Snacks",
        ["Tea", "Coffee", "Bread"],
        "Dinner",
        ["Dal", "Rice", "Chapati", "Sabji"],
    ],
    [
        "Breakfast",
        [
            "Poha",
            "Tea",
            "Coffee",
        ],
        "Lunch",
        ["Dal", "Rice", "Chapati", "Sabji"],
        "Snacks",
        ["Tea", "Coffee", "Bread"],
        "Dinner",
        ["Dal", "Rice", "Chapati", "Sabji"],
    ],
    [
        "Breakfast",
        [
            "Upma",
            "Tea",
            "Coffee",
        ],
        "Lunch",
        ["Dal", "Rice", "Chapati", "Sabji"],
        "Snacks",
        ["Tea", "Coffee", "Bread"],
        "Dinner",
        ["Dal", "Rice", "Chapati", "Sabji"],
    ],
    [
        "Breakfast",
        [
            "Bread",
            "Butter",
            "Tea",
            "Coffee",
        ],
        "Lunch",
        ["Dal", "Rice", "Chapati", "Sabji"],
        "Snacks",
        ["Tea", "Coffee", "Bread"],
        "Dinner",
        ["Dal", "Rice", "Chapati", "Sabji"],
    ],
    [
        "Breakfast",
        [
            "Bread",
            "Jam",
            "Tea",
            "Coffee",
        ],
        "Lunch",
        ["Dal", "Rice", "Chapati", "Sabji"],
        "Snacks",
        ["Tea", "Coffee", "Bread"],
        "Dinner",
        ["Dal", "Rice", "Chapati", "Sabji"],
    ],
    [
        "Breakfast",
        [
            "Bread",
            "Butter",
            "Jam",
            "Tea",
            "Coffee",
        ],
        "Lunch",
        ["Dal", "Rice", "Chapati", "Sabji"],
        "Snacks",
        ["Tea", "Coffee", "Bread"],
        "Dinner",
        ["Dal", "Rice", "Chapati", "Sabji"],
    ],
    [
        "Breakfast",
        [
            "Bread",
            "Butter",
            "Jam",
            "Tea",
            "Coffee",
        ],
        "Lunch",
        ["Dal", "Rice", "Chapati", "Sabji"],
        "Snacks",
        ["Tea", "Coffee", "Bread"],
        "Dinner",
        [
            "Dal",
            "Rice",
            "Chapati",
            "Sabji",
        ],
    ],
]


def index(request):
    form = add_data(request.POST or None)
    if form.is_valid():
        form.save()
        form = add_data()
        return HttpResponseRedirect("../success/")
    dict5 = {"form": form}
    current_day_menu = menu[day]
    flattened_menu = []

    for meal, items in zip(current_day_menu[::2], current_day_menu[1::2]):
        for item in items:
            flattened_menu.append((meal, item))

    data = {"menu": flattened_menu}

    return render(request, "index.html", {"form": form, "data": data})


def success(request):
    quote_text, quote_author = get_random_quote()
    context = {"quote_text": quote_text, "quote_author": quote_author}
    return render(request, "success.html", context)


def results(request):
    num_rows = Details.objects.count()

    lunch_yes_count = Details.objects.filter(lunch="Yes").count()
    dinner_yes_count = Details.objects.filter(dinner="Yes").count()

    context = {
        "num_rows": num_rows,
        "lunch_yes_count": lunch_yes_count,
        "dinner_yes_count": dinner_yes_count,
    }

    return render(request, "results.html", context)
