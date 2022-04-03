import requests
import json
from config import KEYS, URL


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(
                f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = KEYS[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = KEYS[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(
                f'Не удалось обработать количество {amount}')

        r = requests.get(f'{URL}?fsym={quote_ticker}&tsyms={base_ticker}')
        base_price = json.loads(r.content)[KEYS[base]]
        base_total = round(float(amount) * base_price, 2)
        return base_total
