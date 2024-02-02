from django.db import models

options = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class Details(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    lunch = models.CharField(max_length=35, choices=options)
    dinner = models.CharField(max_length=35, choices=options)
