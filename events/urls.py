from django.urls import path
from .views import LoginView, EventListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='api_login'),
    path('events/', EventListView.as_view(), name='api_events'),
]
