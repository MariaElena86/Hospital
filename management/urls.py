from django.urls import path

from management.views import MatchView

urlpatterns = [
    path('', MatchView.as_view(), name='match')
]