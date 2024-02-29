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


class ValuesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("date", "lunch", "dinner", "total")

    def get_date(self, obj):
        return obj.date

    def get_lunch(self, obj):
        return obj.lunch

    def get_dinner(self, obj):
        return obj.dinner

    def get_total(self, obj):
        return obj.total

    get_date.short_description = "Date"
    get_lunch.short_description = "Lunch"
    get_dinner.short_description = "Dinner"
    get_total.short_description = "Total"


admin.site.register(Details, DetailsAdmin)
admin.site.register(Values)
