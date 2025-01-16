import requests

def get_exchange_rate(source_currency, target_currency):
    api_url = f'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(api_url)
    data = response.json()
    if source_currency != 'RUB':
        sc = data['Valute'][source_currency]['Value']
    else:
        sc = 1
    if target_currency != 'RUB':
        tc = data['Valute'][target_currency]['Value']
    else:
        tc = 1

    return sc/tc