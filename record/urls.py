from django.urls import path
from record.views import (index, scoreboard, daily_goal_record, get_form_daily_goals_check, 
                          category_record, edit_category_record, delete_category_record, gift_cards
                          )

urlpatterns = [
    path('', index, name='home'),
    path('scoreboard', scoreboard, name='scoreboard'),
    path('daily-goal-record', daily_goal_record, name='daily_goal_record'),
    path('get_form_daily_goals_check/<str:date>/', get_form_daily_goals_check, name='get_form_daily_goals_check'),
    path('category-record',category_record, name='category_record'),
    path('category-record/edit/<int:record_id>/', edit_category_record, name='edit_category_record'),
    path('category-record/delete/<int:record_id>/', delete_category_record, name='delete_category_record'),
    path('gift-cards', gift_cards, name='gift_cards'),
]