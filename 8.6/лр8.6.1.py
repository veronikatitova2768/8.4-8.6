import requests

url = 'https://wttr.in'  # URL сервиса погоды

weather_parameters = {
    '0': '',
    'T': ''  # добавляем параметр `T`, чтобы вернулся чёрно-белый текст
}

# Отправляем GET-запрос с параметрами
response = requests.get(url, params=weather_parameters)

# Печатаем ответ от сервера
print(response.text)
