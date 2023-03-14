from django.contrib import admin
from record.models import User, Daily_Objective, Rule, Logbook, Category, Category_Record, Goal


class UsersList(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    list_display_links = ("id", "name", "email")
    search_fields = ("name", "email",)
admin.site.register(User, UsersList)
    
class CategoriesList(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
admin.site.register(Category, CategoriesList)

class CategoryRecordsList(admin.ModelAdmin):
    list_display = ("id", "fk_category", "description", "date", "fk_user")
    list_display_links = ("id", "fk_category", "description")
    list_filter = ("fk_category","fk_category","fk_user",)
    list_per_page = 10
    search_fields = ("description",)
admin.site.register(Category_Record, CategoryRecordsList)

class GoalsList(admin.ModelAdmin):
    list_display = ("id", "description", "creation_date", "conclusion_date", "done", "fk_user", "reward")
    list_display_links = ("id", "description")
    list_filter = ("fk_user",)
    list_per_page = 10
    search_fields = ("description",)
    list_editable = ("done",)
admin.site.register(Goal, GoalsList)

class DailyObjsList(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
admin.site.register(Daily_Objective, DailyObjsList)

class RulesList(admin.ModelAdmin):
    list_display = ("id", "description", "reward")
    list_display_links = ("id", "description")
    search_fields = ("description",)
admin.site.register(Rule, RulesList)

class logBooksList(admin.ModelAdmin):
    list_display = ("date", "fk_daily_obj", "fk_user")
    list_display_links = ("date", "fk_daily_obj")
    search_fields = ("date",)
    list_filter = ("fk_daily_obj", "fk_user",)
    list_per_page = 10
admin.site.register(Logbook, logBooksList)

#class BooksAndCoursesList(admin.ModelAdmin):
#    list_display = ("id", "name", "conclusion_date")
#    list_display_links = ("id", "name")
#    search_fields = ("name",)
#admin.site.register(Book, BooksAndCoursesList)
#admin.site.register(Course, BooksAndCoursesList)

