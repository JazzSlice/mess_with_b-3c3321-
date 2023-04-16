import urllib.parse
import requests

user_query = 'как стать бэкенд-разработчиком'
query = user_query.split(' ')
modyfied_query = '%20'.join(query)
url = 'https://yandex.ru/search/?text=' +  f'{modyfied_query}'

print(url,'\n', urllib.parse.quote(user_query))

url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'

split_query = url.split('=')
question = urllib.parse.unquote(split_query[1])

print(question)

phrase = 'какой-то текст'
parsed = urllib.parse.quote(phrase)
print(parsed)

# https://wttr.in/:help?lang=ru dockumentation

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
    'lang': 'ru'
}

response = requests.get(url, params=weather_parameters)

print(response.text)