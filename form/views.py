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
                "Easy Chana Masala Recipe In Pressure cooker – How To Make Chana Masala Recipe.jpg",
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
            ["Chapati Breads.jpeg", "Chapati"],
            [
                "White Peas Potato Curry Recipe - Vatana Aloo Masala Recipe.jpg",
                "Muttar Masala",
            ],
            ["veg jhal pyaza.jpg", "Bhindi Aloo Bujjiya"],
            ["pulao.jpg", "Pulao"],
            [
                "Organic SAMBHAR MASALA - Curry Masala - Sambaar Masala.jpeg",
                "Masala Sambar",
            ],
            ["mixed veg poriyal.jpg", "Poriyal"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Grlic Rasam",
            ],
            ["What Are The Benefits Of Buttermilk_.jpg", "Butter Milk"],
            [
                "Tomato Dal Recipe, Andhra Tomato Pappu (Step By Step & Video).jpg",
                "Tomato dal",
            ],
        ],
        "Snacks",
        [
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/coffee",
            ],
            [
                "Veg Puff Recipe - Vegetable Puff Recipe with Step By Step Photos.jpg",
                "Sweet Puff",
            ],
        ],
        "Dinner",
        [
            ["Chapati Breads.jpeg", "Chapati"],
            ["rice.jpeg", "Rice"],
            ["Dal Tadka Recipe.jpg", "Dal Tadka"],
            ["khadai chicken.jpg", "Butter Chicken Masala"],
            [
                "Paneer Butter Masala - Paneer Recipe Two Ways - Cubes N Juliennes.jpg",
                "Paneer Butter Masala",
            ],
            ["Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg", "Rasam"],
            [
                "Banana fruit close up stock vector_ Illustration of farm - 57102709.jpg",
                "Salad/Banana",
            ],
            [
                "Mutton curry recipe _ south Indian Mutton gravy Jinoo's Kitchen.jpg",
                "Chicken Gravy",
            ],
            ["milk.jpeg", "Milk"],
        ],
    ],
    [
        "Breakfast",
        [
            ["milk.jpeg", "Cocount Milk"],
            ["Easy strawberry jam.jpeg", "Bread/Butter/Jam"],
            ["Idiyappam Recipe (Nool Puttu).jpeg", "Idiyappam"],
            [
                "Easy Chana Masala Recipe In Pressure cooker – How To Make Chana Masala Recipe.jpg",
                "Chana Masala",
            ],
            ["Chapati Breads.jpeg", "Chapati"],
            [
                "Coconut Chutney Recipe, How to make white coconut chutney.jpeg",
                "White Khurma Chutney",
            ],
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Cofee/Milk",
            ],
        ],
        "Lunch",
        [
            ["Chapati Breads.jpeg", "Chapati"],
            ["rice.jpeg", "Rice"],
            ["Aloo Bhaji [Indian Spiced Potatoes].jpg", "Aloo Ghobi"],
            ["pulao.jpg", "Onion Pulao"],
            [
                "Tomato Dal Recipe, Andhra Tomato Pappu (Step By Step & Video).jpg",
                "Punjabi Dal",
            ],
            ["kadi pakoda recipe.jpg", "Kadi Pakoda"],
            ["Yam Varuval.jpg", "Yam Varuval"],
            ["What Are The Benefits Of Buttermilk_.jpg", "Butter Milk"],
            ["Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg", "Rasam"],
        ],
        "Snacks",
        [
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee",
            ],
            ["panipuri.jpeg", "Pani Poori"],
            ["sundal.jpg", "Chena Sundal"],
        ],
        "Dinner",
        [
            ["pongal sweet.jpg", "Millet Sweet"],
            ["chole bhature.jpg", "Chole Bhature"],
            [
                "Easy Chana Masala Recipe In Pressure cooker – How To Make Chana Masala Recipe.jpg",
                "Chole Masala",
            ],
            ["rice.jpeg", "rice"],
            [
                "Tomato Dal Recipe, Andhra Tomato Pappu (Step By Step & Video).jpg",
                "Tomato Dal",
            ],
            [
                "Premium Photo _ Idly or idli south indian main breakfast item which is beautifully arranged in a fresh green banana leaf on white background.jpg",
                "Idly/sambar",
            ],
            ["Coconut Chutney For Dosa And Idli.jpg", "Cocunut Chutney"],
            ["Podi idli is a quick and easy snack from South India.jpg", "Idli Podi"],
            [
                "Mutton curry recipe _ south Indian Mutton gravy Jinoo's Kitchen.jpg",
                "Mutton Gravy",
            ],
            ["milk.jpeg", "Salad/Milk"],
        ],
    ],
    [
        "Breakfast",
        [
            ["Easy strawberry jam.jpeg", "Bread/Butter/Jam"],
            ["Chapati Breads.jpeg", "Chapati"],
            ["Rajma Recipe _ Rajma Masala.jpg", "Rajma Masala"],
            [
                "Premium Photo _ Idly or idli south indian main breakfast item which is beautifully arranged in a fresh green banana leaf on white background.jpg",
                "Dosa/Idli/Sambar",
            ],
            ["Coconut Chutney For Dosa And Idli.jpg", "Chutney"],
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/coffee/milk",
            ],
        ],
        "Lunch",
        [
            ["gulab jamun.jpg", "Dry Jamun"],
            ["Bread Halwa Recipe.jpeg", "Bread Halwa"],
            ["gobhi.jpeg", "Capsicum Gobi Curry"],
            ["Dal Tadka Recipe.jpg", "Dal Tadka"],
            ["mushroom biryani.jpg", "Veg Briyani"],
            ["Veg Raita _ Vegetable Raita.jpg", "Mix Raita"],
            ["Bisbelabath Rice.jpg", "Bisibelabath/Curd Rice"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Tomato Rasam",
            ],
        ],
        "Snacks",
        [
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee",
            ],
            ["Sambar Vada.jpg", "Sambar Vada"],
        ],
        "Dinner",
        [
            ["Chapati Breads.jpeg", "Millet Chappati"],
            [
                "Veg Manchurian Recipe with Manchurian Sauce - Swasthi's Recipes.jpg",
                "Veg Manchurian",
            ],
            ["Veg Fried Rice _ Indian Style Fried Rice.jpg", "Veg Noodles/Fried Rice"],
            ["Dal Maharani.jpg", "Dal Maharani"],
            [
                "Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg",
                "Sambhar/Rasam",
            ],
            [
                "Mutton curry recipe _ south Indian Mutton gravy Jinoo's Kitchen.jpg",
                "Chicken Gravy",
            ],
            ["milk.jpeg", "Milk"],
            ["rice.jpeg", "Rice"],
        ],
    ],
    [
        "Breakfast",
        [
            ["Easy strawberry jam.jpeg", "Bread/Butter/Jam"],
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee",
            ],
            ["Chapati Breads.jpeg", "Chapati"],
            ["khurma.jpeg", "Veg Khruma"],
            ["Medu Vada Recipe.jpeg", "Pongal Vada"],
            ["Coconut Chutney For Dosa And Idli.jpg", "Chutney/Sambar"],
        ],
        "Lunch",
        [
            ["poori.jpeg", "Poori"],
            [
                "White Peas Potato Curry Recipe - Vatana Aloo Masala Recipe.jpg",
                "White Peas Curry",
            ],
            [
                "Indian potato curry - Quick & easy 20 minutes recipe.jpg",
                "Aloo Thindeli",
            ],
            ["pulao.jpg", "Kashmiri Pulao"],
            ["rice.jpeg", "Rice"],
            ["Dal Tadka Recipe.jpg", "Dal Fry"],
            ["Karakozhambu.jpg", "KaraKozhambu"],
            ["Kootu _ Carrot Kootu.jpg", "Kootu(Cabbage)"],
            ["Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg", "Rasam"],
            ["What Are The Benefits Of Buttermilk_.jpg", "Butter Milk"],
        ],
        "Snacks",
        [
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee",
            ],
            ["Brownie Butter Cake - thick brownie and rich….jpg", "Cake"],
        ],
        "Dinner",
        [
            ["madras paratha.jpg", "Punjabi Paratha"],
            ["patato fry.jpg", "Potato Fry"],
            ["rice.jpeg", "Rice"],
            ["veg jhal pyaza.jpg", "Veg Jhal Pyaza"],
            [
                "Tomato Dal Recipe, Andhra Tomato Pappu (Step By Step & Video).jpg",
                "Bagara Dal",
            ],
            ["Podi idli is a quick and easy snack from South India.jpg", "Idli Podi"],
            [
                "Instant Sambar Without Dal For Idli, Dosa - Easy Tiffin Sambar Recipe.jpg",
                "Kathamba Sambar",
            ],
            [
                "Banana fruit close up stock vector_ Illustration of farm - 57102709.jpg",
                "Salad/Banana",
            ],
            [
                "Mutton curry recipe _ south Indian Mutton gravy Jinoo's Kitchen.jpg",
                "Chicken Gravy",
            ],
            ["milk.jpeg", "Milk"],
        ],
    ],
    [
        "Breakfast",
        [
            ["Easy strawberry jam.jpeg", "Bread/Butter/Jam"],
            ["chole bhature.jpg", "Chole Bhature"],
            [
                "Easy Chana Masala Recipe In Pressure cooker – How To Make Chana Masala Recipe.jpg",
                "Chennai Masala",
            ],
            ["upma.jpeg", "Samba Rava Upma"],
            ["Coconut Chutney For Dosa And Idli.jpg", "Coconut Chutney"],
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee/Milk",
            ],
        ],
        "Lunch",
        [
            ["Chapati Breads.jpeg", "Chapathi"],
            ["khadai chicken.jpg", "Kadai Chicken"],
            [
                "Paneer Butter Masala - Paneer Recipe Two Ways - Cubes N Juliennes.jpg",
                "Puneer Butter Masala",
            ],
            ["Dal Tadka Recipe.jpg", "Dal Tadka"],
            ["pulao.jpg", "Mint Pulao"],
            ["rice.jpeg", "Rice"],
            ["Pepper Rasam Recipe (Milagu Rasam) - Spice Up The Curry.jpg", "Rasam"],
            ["What Are The Benefits Of Buttermilk_.jpg", "Butter Milk"],
            ["mixed veg poriyal.jpg", "Mix Veg Poriyal"],
        ],
        "Snacks",
        [
            [
                "Download Cup of coffee on glass table on white background_ for free.jpg",
                "Tea/Coffee",
            ],
            ["Masala Corn _ Easy and Healthy Snack Recipe.jpeg", "Corn/Bajji "],
        ],
        "Dinner",
        [
            [
                "Punjabi Aloo Paratha Recipe (with step by step photos).jpg",
                "Aloo Paratha",
            ],
            ["Veg Raita _ Vegetable Raita.jpg", "Masala Curd"],
            ["Dal Tadka Recipe.jpg", "Hara Moong Dal Tadka"],
            ["cone ice cream.jpg", "Ice Cream"],
            [
                "Mutton curry recipe _ south Indian Mutton gravy Jinoo's Kitchen.jpg",
                "Chicken Gravy",
            ],
            [
                "Banana fruit close up stock vector_ Illustration of farm - 57102709.jpg",
                "Salad/Banana",
            ],
            ["mixed veg poriyal.jpg", "Poriyal"],
            [
                "Instant Sambar Without Dal For Idli, Dosa - Easy Tiffin Sambar Recipe.jpg",
                "Kathamba Sambar",
            ],
            ["milk.jpeg", "Milk"],
            ["rice.jpeg", "Rice"],
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
