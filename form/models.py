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

    def save(self, *args, **kwargs):
        last_record = Details.objects.last()
        if last_record and last_record.date != self.date:
            # Reset the database or perform any desired action
            Details.objects.all().delete()

        super().save(*args, **kwargs)

