from django.db import models

options = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class Details(models.Model):
    lunch = models.CharField(max_length=35, choices=options)
    dinner = models.CharField(max_length=35, choices=options)
