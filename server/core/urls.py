# core/urls.py
from django.urls import path
from . import views  # this imports views.py from the core folder

urlpatterns = [
    path('funds/', views.fund_list, name='fund_list'),
]
