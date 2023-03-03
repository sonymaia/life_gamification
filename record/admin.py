from django.contrib import admin
from record.models import Book, Course, Daily_Objective, Rule, Logbook


class BooksAndCoursesList(admin.ModelAdmin):
    list_display = ("id", "name", "conclusion_date")
    list_display_links = ("id", "name")
    search_fields = ("name",)
admin.site.register(Book, BooksAndCoursesList)
admin.site.register(Course, BooksAndCoursesList)


class DailyObjsList(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
admin.site.register(Daily_Objective, DailyObjsList)

class RulesList(admin.ModelAdmin):
    list_display = ("id", "description", "award")
    list_display_links = ("id", "description")
    search_fields = ("description",)
admin.site.register(Rule, RulesList)

class logBooksList(admin.ModelAdmin):
    list_display = ("date", "fk_daily_obj")
    list_display_links = ("date", "fk_daily_obj")
    search_fields = ("date",)
admin.site.register(Logbook, logBooksList)

