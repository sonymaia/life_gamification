from django.urls import path
from record.views import index, scoreboard

urlpatterns = [
    path('', index),
    path('scoreboard.html', scoreboard),

]