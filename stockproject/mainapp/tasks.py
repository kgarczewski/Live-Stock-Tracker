from asgiref.sync import async_to_sync
from celery import shared_task
from yahoo_fin.stock_info import *
from .models import Stock
from django.forms.models import model_to_dict
from channels.layers import get_channel_layer


channel_layer = get_channel_layer()

@shared_task
def get_coins_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=pln&order=market_cap_desc&per_page=5&page=1&sparkline=false'

    data = requests.get(url).json()
    stocks = []
    for stock in data:
        obj, created = Stock.objects.get_or_create(name=stock['name'])
        obj.name = stock['name']
        obj.symbol = stock['symbol']
        if obj.price > stock['current_price']:
            state = 'fall'
        elif obj.price < stock['current_price']:
            state = 'raise'
        elif obj.price == stock['current_price']:
            state = 'same'
        obj.price = stock['current_price']
        obj.image = stock['image']

        obj.save()

        new_data = model_to_dict(obj)
        new_data.update({'state': state})
        stocks.append(new_data)

    async_to_sync(channel_layer.group_send)('stocks', {'type': 'send_new_data', 'text': stocks})


