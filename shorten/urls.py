from django.urls import path
from shorten.views import EncurtadorListView, EncurtadorCreateView, EncurtadorDetailView

urlpatterns = [
    path('urls/', EncurtadorListView.as_view(), name='list_urls'),
    path('<slug:slug>/', EncurtadorDetailView.as_view(), name='redirect'),
    path('', EncurtadorCreateView.as_view(), name='home'),
]
