from django.urls import path
from shorten.views import EncurtadorListView, EncurtadorCreateView

urlpatterns = [
    path('shorten/', EncurtadorCreateView.as_view(), name='new_url'),
    path('', EncurtadorListView.as_view(), name='home'),
]
