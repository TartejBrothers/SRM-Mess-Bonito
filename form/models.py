from django.db import models
from datetime import datetime
from django.db.models import Count, Q
from django.utils import timezone
from django.db.models import F

options = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class Values(models.Model):
    date = models.DateField(unique=True)
    lunch = models.IntegerField(default=0)
    dinner = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

class Wasteage(models.Model):
    date = models.DateField(unique=True)
    lunch = models.IntegerField(default=0)
    dinner = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

class Details(models.Model):
    email = models.CharField(max_length=254)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    lunch = models.CharField(max_length=35, choices=options)
    dinner = models.CharField(max_length=35, choices=options)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.now().date()

        last_record = Details.objects.order_by("-date").first()
        if last_record and last_record.date != self.date:
            results_data = results()
            if results_data:
                Values.objects.update_or_create(
                    date=results_data["date"],
                    defaults={
                        "lunch": results_data.get("lunch", 0),
                        "dinner": results_data.get("dinner", 0),
                        "total": results_data.get("total", 0),
                    },
                )
            Details.objects.all().delete()
        super().save(*args, **kwargs)


def results():
    last_record = Details.objects.order_by("-date").first()
    if last_record and last_record.date != timezone.now().date():
        lunch_count = Details.objects.filter(lunch="Yes").count()
        dinner_count = Details.objects.filter(dinner="Yes").count()
        print("Counts=", lunch_count, dinner_count)
        num_rows = Details.objects.count()

        last_date_record = Details.objects.order_by("-date").first()
        if last_date_record:
            last_date = last_date_record.date
            print("Last Date:", last_date)
        else:
            print("No records found")
            return {}

        total_count = num_rows
        return {
            "date": last_date,
            "lunch": lunch_count,
            "dinner": dinner_count,
            "total": total_count,
        }
    return {}
