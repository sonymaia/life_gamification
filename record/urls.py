from django.urls import path
from record.views import index, scoreboard, daily_goal_record, get_form_daily_goals_check, category_record

urlpatterns = [
    path('', index),
    path('scoreboard.html', scoreboard, name='scoreboard'),
    path('daily-goal-record.html', daily_goal_record, name='daily_goal_record'),
    path('get_form_daily_goals_check/<str:date>/', get_form_daily_goals_check, name='get_form_daily_goals_check'),
    path('category-record.html',category_record, name='category_record'),
]