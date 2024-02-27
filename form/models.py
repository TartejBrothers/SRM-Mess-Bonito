from django.db import models
from datetime import datetime
from django.db.models import Count, Q

options = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class Values(models.Model):
    date = models.DateField(auto_now_add=True)
    lunch = models.IntegerField()
    dinner = models.IntegerField()
    total = models.IntegerField()


class Details(models.Model):
    email = models.CharField(max_length=254)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    lunch = models.CharField(max_length=35, choices=options)
    dinner = models.CharField(max_length=35, choices=options)

    def save(self, *args, **kwargs):
        self.date = datetime.now().date()
        last_record = Details.objects.last()
        if last_record and last_record.date != self.date:
            results_data = results()
            Values.objects.update_or_create(
                date=results_data["date"],
                defaults={
                    "lunch": results_data["lunch"],
                    "dinner": results_data["dinner"],
                    "total": results_data["total"],
                },
            )
            Details.objects.all().delete()
        super().save(*args, **kwargs)


def results():
    last_record = Details.objects.last()
    if last_record and last_record.date != datetime.now().date():

        lunch_counts = Details.objects.values("date").annotate(
            lunch_count=Count("pk", filter=Q(lunch="Yes"))
        )
        dinner_counts = Details.objects.values("date").annotate(
            dinner_count=Count("pk", filter=Q(dinner="Yes"))
        )
        num_rows = Details.objects.count()
        for lunch_data, dinner_data in zip(lunch_counts, dinner_counts):
            date = lunch_data["date"]
            lunch_count = lunch_data["lunch_count"]
            dinner_count = dinner_data["dinner_count"]
            total_count = num_rows
            date = datetime.strptime(date, "%Y-%m-%d").date()

            # Save the Values object
            Values.objects.update_or_create(
                date=date,
                defaults={
                    "lunch": lunch_count,
                    "dinner": dinner_count,
                    "total": total_count,
                },
            )
    return {}
