from django.urls import path
from record.views import index, scoreboard, daily_goal_record

urlpatterns = [
    path('', index),
    path('scoreboard.html', scoreboard),
    path('daily-goal-record.html', daily_goal_record),
]