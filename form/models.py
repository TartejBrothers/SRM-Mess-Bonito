from django.db import models
from datetime import datetime

options = (
    ("Yes", "Yes"),
    ("No", "No"),
)


class Details(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    lunch = models.CharField(max_length=35, choices=options)
    dinner = models.CharField(max_length=35, choices=options)

    def save(self, *args, **kwargs):
        # Set the date to the current date without considering time
        self.date = datetime.now().date()

        last_record = Details.objects.last()
        if last_record:
            print("Last date:", last_record.date)
            print("Self Date: ", self.date)
        if last_record and last_record.date != self.date:
            Details.objects.all().delete()

        super().save(*args, **kwargs)
