from django.urls import path
from record.views import index

urlpatterns = [
    path('', index)
]