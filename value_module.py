import requests
import json
import datetime


def value_moneys(sum_money, Charcode1, Charcode2):
    response = requests.get(
        'https://www.cbr-xml-daily.ru/daily_json.js'
    )
    values = response.json()
    if Charcode1 == 'RUB':
        curse1 = 1
    else:
        curse1 = float(values['Valute'][Charcode1]['Value']) / int(values['Valute'][Charcode1]['Nominal'])
    if Charcode2 == 'RUB':
        curse2 = 1
    else:
        curse2 = float(values['Valute'][Charcode2]['Value']) / int(values['Valute'][Charcode2]['Nominal'])
    return float(sum_money) * curse1 / curse2
