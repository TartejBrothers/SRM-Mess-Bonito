from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import add_data
from .quotes import get_random_quote
from .models import Details

from datetime import datetime

day = datetime.now().weekday()

menu = [
    [
        "Breakfast",
        [
            ["roti.jpeg", "Roti"],
            ["tea.jpeg", "Tea"],
            ["coffee.jpeg", "Coffee"],
        ],
        "Lunch",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
        "Snacks",
        [["tea.jpeg", "Tea"], ["coffee.jpeg", "Coffee"], ["bread.jpeg", "Bread"]],
        "Dinner",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
    ],
    [
        "Breakfast",
        [
            ["roti.jpeg", "Roti"],
            ["tea.jpeg", "Tea"],
            ["coffee.jpeg", "Coffee"],
        ],
        "Lunch",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
        "Snacks",
        [["tea.jpeg", "Tea"], ["coffee.jpeg", "Coffee"], ["bread.jpeg", "Bread"]],
        "Dinner",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
    ],
    [
        "Breakfast",
        [
            ["roti.jpeg", "Roti"],
            ["tea.jpeg", "Tea"],
            ["coffee.jpeg", "Coffee"],
        ],
        "Lunch",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
        "Snacks",
        [["tea.jpeg", "Tea"], ["coffee.jpeg", "Coffee"], ["bread.jpeg", "Bread"]],
        "Dinner",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
    ],
    [
        "Breakfast",
        [
            ["roti.jpeg", "Roti"],
            ["tea.jpeg", "Tea"],
            ["coffee.jpeg", "Coffee"],
        ],
        "Lunch",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
        "Snacks",
        [["tea.jpeg", "Tea"], ["coffee.jpeg", "Coffee"], ["bread.jpeg", "Bread"]],
        "Dinner",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
    ],
    [
        "Breakfast",
        [
            ["roti.jpeg", "Roti"],
            ["tea.jpeg", "Tea"],
            ["coffee.jpeg", "Coffee"],
        ],
        "Lunch",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
        "Snacks",
        [["tea.jpeg", "Tea"], ["coffee.jpeg", "Coffee"], ["bread.jpeg", "Bread"]],
        "Dinner",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
    ],
    [
        "Breakfast",
        [
            ["roti.jpeg", "Roti"],
            ["tea.jpeg", "Tea"],
            ["coffee.jpeg", "Coffee"],
        ],
        "Lunch",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
        "Snacks",
        [["tea.jpeg", "Tea"], ["coffee.jpeg", "Coffee"], ["bread.jpeg", "Bread"]],
        "Dinner",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
    ],
    [
        "Breakfast",
        [
            ["roti.jpeg", "Roti"],
            ["tea.jpeg", "Tea"],
            ["coffee.jpeg", "Coffee"],
        ],
        "Lunch",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
        ],
        "Snacks",
        [["tea.jpeg", "Tea"], ["coffee.jpeg", "Coffee"], ["bread.jpeg", "Bread"]],
        "Dinner",
        [
            ["dal.jpeg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["roti.jpeg", "roti"],
            ["sabji.jpeg", "Sabji"],
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
