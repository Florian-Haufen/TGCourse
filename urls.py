import requests

# Курс доллара (Сегодняшний)
def get_doll():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['USD']['Value']

# Курс доллара (Вчерашний)
def get_doll_previous():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['USD']['Previous']

# Курс евро (Сегодняшний)
def get_euro():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['EUR']['Value']

# Курс евро (Вчерашний)
def get_euro_previous():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['EUR']['Previous']

# Курс юаня (Сегодняшний)
def get_yun():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['CNY']['Value']

# Курс юаня (Вчерашний)
def get_yun_previous():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['CNY']['Previous']

# Курс фунта (Сегодняшний)
def get_funt():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['GBP']['Value']

# Курс фунта (Вчерашний)
def get_funt_previous():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response_1 = requests.get(url)
    data = response_1.json()
    return data['Valute']['GBP']['Previous']