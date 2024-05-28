import requests

url = 'https://wttr.in'  # URL сервиса погоды

weather_parameters = {
    '0': '',
    'T': '',  # чёрно-белый текст
    'M': '',  # скорость ветра в м/с
    'lang': 'ru'  # язык прогноза - русский
}

# Отправляем GET-запрос с параметрами
response = requests.get(url, params=weather_parameters)

# Печатаем ответ от сервера
print(response.text)
