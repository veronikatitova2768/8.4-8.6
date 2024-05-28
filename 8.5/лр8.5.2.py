import urllib.parse

url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'

# Получаем закодированный текст запроса из URL
encoded_query = url.split('=')[1]

# Декодируем запрос
decoded_query = urllib.parse.unquote(encoded_query)

# Печатаем декодированный запрос
print(decoded_query)
