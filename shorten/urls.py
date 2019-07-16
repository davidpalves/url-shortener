from django.urls import path
from shorten.views import EncurtadorListView, EncurtadorCreateView
from shorten.views import EncurtadorDetailView, EncurtadorDeleteView

urlpatterns = [
    path('<slug:slug>/delete/', EncurtadorDeleteView.as_view(), name='delete'),
    path('urls/', EncurtadorListView.as_view(), name='list_urls'),
    path('<slug:slug>/', EncurtadorDetailView.as_view(), name='redirect'),
    path('', EncurtadorCreateView.as_view(), name='home'),
]
