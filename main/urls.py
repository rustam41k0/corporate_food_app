from django.urls import path
from .views import MainPageView, CreateOrderView, HistoryOrderView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('add-order', CreateOrderView.as_view(), name='create-order'),
    path('history', HistoryOrderView.as_view(), name='history'),
]
