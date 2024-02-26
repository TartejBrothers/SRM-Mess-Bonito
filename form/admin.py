from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Details, Values


class DetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("email", "date", "time", "get_lunch", "get_dinner")

    def get_lunch(self, obj):
        return obj.lunch

    def get_dinner(self, obj):
        return obj.dinner

    get_lunch.short_description = "Lunch"
    get_dinner.short_description = "Dinner"


admin.site.register(Details, DetailsAdmin)
admin.site.register(Values)