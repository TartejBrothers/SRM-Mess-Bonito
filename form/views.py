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
            ["Easy strawberry jam.jpeg", "Bread/Butter"],
            ["Kodo Millet Dosa _ Varagu arisi dosa.jpeg", "Millet dosa"],
            ["Podi idli is a quick and easy snack from South India.jpg", "Idly Podi"],
            ["Chapati Breads.jpeg", "Chapati"],
            ["Khurmi - Chhattisgarh.jpeg", "White Khururna"],
            ["Boiled Egg.jpg", "Boiled egg"],
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/coffee/milk",
            ],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "sambhar/oil",
            ],
        ],
        "Lunch",
        [
            ["Dal Tadka Recipe.jpg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["Chapati Breads.jpeg", "chapati"],
            ["Rajma Recipe _ Rajma Masala.jpg", "rajma masala"],
            ["pulao.jpg", "Jeera pulao"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Arachivitta sambar",
            ],
            ["bagara dal.jpg", "Panchratna Dal"],
            [
                "White Peas Potato Curry Recipe - Vatana Aloo Masala Recipe.jpg",
                "Drumstick Brinjal Mochai",
            ],
            ["Aloo Bhaji [Indian Spiced Potatoes].jpg", "Dum aloo"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Pineapple Rasam",
            ],
            ["What Are The Benefits Of Buttermilk_.jpg", "Butter Milk"],
        ],
        "Snacks",
        [
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee",
            ],
            ["Pav Bhaji.jpg", "Pav Bhaji"],
        ],
        "Dinner",
        [
            ["Dal Tadka Recipe.jpg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["Chapati Breads.jpeg", "Chapati"],
            ["veg jhal pyaza.jpg", "Sabji"],
            ["madras paratha.jpg", "Madras Paratha"],
            [
                "Matar Paneer Recipe (Easy, Healthy Punjabi Mutter Paneer Masala).jpg",
                "Mattar panner Masala",
            ],
            ["Podi idli is a quick and easy snack from South India.jpg", "Idli podi"],
            [
                "Coconut Chutney Recipe _ Easy Chutney Recipe and Tips to select a good coconut.jpg",
                "Special chutney",
            ],
            ["bagara dal.jpg", "Hara Moong dal"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Sambhar/rasam",
            ],
            [
                "Banana fruit close up stock vector_ Illustration of farm - 57102709.jpg",
                "fish gravy/banana",
            ],
            ["milk.jpeg", "milk"],
        ],
    ],
    [
        "Breakfast",
        [
            ["Easy strawberry jam.jpeg", "bread/butter/jam"],
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/coffee/milk",
            ],
            [
                "Coconut Chutney Recipe _ Easy Chutney Recipe and Tips to select a good coconut.jpg",
                "Poori/chutney",
            ],
            ["Veg Semiya Khichdi.jpg", "Semia Veg Kichadi"],
            ["Aloo Matar (Aloo Mattar).jpg", "Dal allo masala"],
        ],
        "Lunch",
        [
            ["sweets.jpg", "sweet"],
            ["Chapati Breads.jpeg", "Millet Chapati"],
            ["curry.jpeg", "Meal curry"],
            ["pulao.jpg", "Bahara Pulao"],
            ["curd rice.jpg", "Rice/Curd rice/Steamed rice"],
            ["Dal Tadka Recipe.jpg", "Dal fry"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Tamoto Rasam",
            ],
            ["pickle.jpeg", "Urulai Peas Roasted Pickels"],
        ],
        "Snacks",
        [
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee",
            ],
            ["Mysore Bonda _ Mysore Bajji _ Bonda Recipe.jpg", "Mysore Bonda"],
        ],
        "Dinner",
        [
            ["madras paratha.jpg", "Punjabi Paratha"],
            [
                "Easy Chana Masala Recipe In Pressure cooker – How To Make Chana Masala Recipe (1).jpg",
                "Black Chenna",
            ],
            ["rice.jpeg", "Rice"],
            ["chilli ghobi.jpeg", "Chilli Gobi Dry"],
            [
                "Plain Dosa Recipe _ How to make dosa for beginners • Chakris Kitchen.jpg",
                "Millet Dosa",
            ],
            ["Podi idli is a quick and easy snack from South India.jpg", "Idly Podi"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Pepper rasam",
            ],
            [
                "Banana fruit close up stock vector_ Illustration of farm - 57102709.jpg",
                "Milok/fruit",
            ],
            [
                "Mutton curry recipe _ south Indian Mutton gravy Jinoo's Kitchen.jpg",
                "Mutton Gravy",
            ],
        ],
    ],
    [
        "Breakfast",
        [
            ["Easy strawberry jam.jpeg", "Bread/butter/jam"],
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/coffee",
            ],
            ["poha.jpeg", "Poha"],
            [
                "Premium Photo _ Idly or idli south indian main breakfast item which is beautifully arranged in a fresh green banana leaf on white background.jpg",
                "Millet Idly",
            ],
            ["Podi idli is a quick and easy snack from South India.jpg", "Idly podi"],
            [
                "Organic SAMBHAR MASALA - Curry Masala - Sambaar Masala.jpeg",
                "Sambar/Mint chutney",
            ],
            ["Indian Masala Omelette Recipe.jpg", "Masala Omlet"],
        ],
        "Lunch",
        [
            ["Chapati Breads.jpeg", "Millet Chapati"],
            ["Dal Tadka Recipe.jpg", "Dal"],
            ["rice.jpeg", "Rice"],
            ["veg curry.jpg", "Curry"],
            ["pulao.jpg", "Pudina pulao"],
            ["bagara dal.jpg", "Dal"],
            ["bagara dal.jpg", "Rice"],
            ["Sambar Recipe.jpeg", "Sambar"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Tomato rasam",
            ],
            ["pickle.jpeg", "Nellikai Thokku"],
            [
                "Mutton curry recipe _ south Indian Mutton gravy Jinoo's Kitchen.jpg",
                "mutton gravy",
            ],
        ],
        "Snacks",
        [
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee",
            ],
            [
                "Oats idli - How to make oats idli _ Healthy breakfast recipe - YouTube.jpg",
                "Oats Idli",
            ],
            ["bun.jpg", "Bun/Salna"],
        ],
        "Dinner",
        [
            ["madras paratha.jpg", "Punjabi Paratha"],
            ["rice.jpeg", "Rice"],
            ["veg curry.jpg", "Sabji"],
            ["Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg", "Kollu"],
            ["madras paratha.jpg", "Madras paratha"],
            ["egg-masala-dosa_01.jpg", "Millet Dosa"],
            ["Sweet_Corn_Sundal_1.jpg", "Sweet Corn Sundal"],
            [
                "Banana fruit close up stock vector_ Illustration of farm - 57102709.jpg",
                "Fruits",
            ],
            ["paneer.jpg", "Paneer Gravy"],
            ["rasam.jpg", "Rasam"],
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
