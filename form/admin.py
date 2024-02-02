# form/admin.py
from django.contrib import admin
from .models import Details


class DetailsAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "get_lunch", "get_dinner")

    def get_lunch(self, obj):
        return obj.lunch

    def get_dinner(self, obj):
        return obj.dinner

    get_lunch.short_description = "Lunch"
    get_dinner.short_description = "Dinner"


admin.site.register(Details, DetailsAdmin)
