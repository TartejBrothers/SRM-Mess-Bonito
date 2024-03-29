from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import add_data
from .quotes import get_random_quote
from .models import Details, Values
import seaborn as sns
import matplotlib
import numpy as np

matplotlib.use("agg")
import matplotlib.pyplot as plt

import pandas as pd
from io import BytesIO
import base64
from datetime import datetime, timedelta
import threading

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


def generate_plot_and_save(values_data):
    dates = [value.date.strftime("%Y-%m-%d") for value in values_data]
    lunch_values = [value.lunch for value in values_data]
    dinner_values = [value.dinner for value in values_data]
    total_values = [value.total for value in values_data]

    plt.figure(figsize=(10, 6))

    bar_width = 0.25
    index = np.arange(len(dates))
    plt.bar(index, lunch_values, bar_width, label="Lunch")
    plt.bar(index + bar_width, dinner_values, bar_width, label="Dinner")
    plt.bar(index + 2 * bar_width, total_values, bar_width, label="Total")
    plt.title("Lunch, Dinner, and Total Values Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(index + bar_width, dates, rotation=45)
    plt.legend()

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    plot_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()

    return plot_data


def plot_matplotlib_graph(request):
    values_data = Values.objects.all()
    plot_data = generate_plot_and_save(values_data)

    return render(request, "plot.html", {"plot_data": plot_data})


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
