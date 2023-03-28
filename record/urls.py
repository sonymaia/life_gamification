from django.urls import path
from record.views import index, scoreboard, daily_goal_record, get_form_daily_goals_check

urlpatterns = [
    path('', index),
    path('scoreboard.html', scoreboard),
    path('daily-goal-record.html', daily_goal_record),
    path('get_form_daily_goals_check/<str:date>/', get_form_daily_goals_check, name='get_form_daily_goals_check'),
]