import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language': 'ru'  # добавляем заголовок для русского языка
}

# Отправляем GET-запрос с параметрами и заголовками
response = requests.get(url, params=weather_parameters, headers=request_headers)

# Печатаем ответ от сервера
print(response.text)
