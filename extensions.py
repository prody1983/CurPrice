import requests
import json
from params import keys

class UsrException(Exception):
    pass

class Req_To_Api:
    @staticmethod
    def get_price(bot, message, from_cur: str, to_cur: str, amount: str):
        try:
            if from_cur not in keys.keys():
                raise UsrException(
                    "Не верный код валюты, цену которой хотим узнать! Посмотрите список валют по команде /values")

            if to_cur not in keys.keys():
                raise UsrException(
                    "Не верный код валюты, в которой надо узнать цену первой валюты! Посмотрите список валют по команде /values")

            try:
                amount = float(amount)
            except ValueError:
                raise UsrException(f"Введите сумму для конвертации! Вы ввели {amount}")

            if amount <= 0:
                raise UsrException("Сумма для конвертации должна быть > 0!")

        except UsrException as e:
            bot.reply_to(message, f'Ошибка обработки входящих параметров: \n {e}')
        except Exception as e:
            bot.reply_to(message, f'Ошибка: \n {e}')
        else:
            headers = {"apikey": "5VO8HTtNwAHT9BZsRk7gzBXYXRB399nq"}

            r = requests.get(
                f'https://api.apilayer.com/exchangerates_data/convert?to={to_cur}&from={from_cur}&amount={amount}',
                headers=headers)

            resp = json.loads(r.content)

            text = resp['result']

            return text