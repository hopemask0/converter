import requests


def get_exchange_rate(source_currency, target_currency):
    api_url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(api_url)
    data = response.json()

    # Проверка, что source_currency и target_currency существуют в данных
    if source_currency != 'RUB' and source_currency not in data['Valute']:
        raise ValueError(f"Валюта {source_currency} не найдена.")
    if target_currency != 'RUB' and target_currency not in data['Valute']:
        raise ValueError(f"Валюта {target_currency} не найдена.")

    # Получение курсов валют
    if source_currency != 'RUB':
        sc = data['Valute'][source_currency]['Value']
    else:
        sc = 1  # RUB всегда равен 1

    if target_currency != 'RUB':
        tc = data['Valute'][target_currency]['Value']
    else:
        tc = 1  # RUB всегда равен 1

    return sc / tc