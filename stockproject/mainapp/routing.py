from django.urls import path

from .consumers import StockConsumer

ws_urlpatterns = [
    path('ws/stock/', StockConsumer.as_asgi())
]