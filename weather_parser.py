# import requests
# import json
# import pprint

# city_name = input("Введите город: ")
# gis_token = ''
# api_url_base = 'https://api.gismeteo.net/v2/search/cities/?lang=ru&query='
# headers = {
#     'X-Gismeteo-Token' : gis_token,
#     'Accept-Encoding' : 'gzip'
# }

# def get_info_about_city(api_url_base_value = api_url_base, requests_headers = None):
#     if requests_headers is None:
#         requests_headers = headers
#     response = requests.get(api_url_base_value + city_name, headers = requests_headers)
#     if response.status_code == 200:
#         return json.loads(response.content.decode('utf-8'))
#     else:
#         return None

# # def get_city_id(city_name):
# #     response = requests.get(api_url_base + city_name, headers=headers)
# #     if response.status_code == 200:
# #         data = json.loads(response.content.decode('utf-8'))
# #         #return data['response']['items'][0]['id']
# #         if city_name == data['response']['items'][0]['name'] and data['response']['items'][0]['name'] is not None:
# #             return data['response']['items'][0]['id']
# #         else:
# #             return 'Произошла ошибка! Проверьте правильность введённого города!'
# #     else:
# #         return 'Ошибка сервера :()'
# #         return None
# def get_city_id(city_name):
#     response = requests.get(api_url_base + city_name, headers=headers)
#     if response.status_code == 200:
#         data = json.loads(response.content.decode('utf-8'))
#         if city_name == data['response']['items'][0]['name'] or city_name == data['response']['items'][0]['sub_district']['name'] :
#             return data['response']['items'][0]['id']
#         else:
#             print('Город не найден :(')
#             return None
#     else:
#         print('Ошибка получения информации :(')
#         return None

# # print(get_city_id(city_name))



# def get_wind_direction(degrees):
#     if degrees is None:
#         return 'Нет данных'
#     else:
#         directions = ["Северный", "Северо-восточный", "Восточный", "Юго-восточный", "Южный", "Юго-западный", "Западный", "Северо-западный", "Северный"]
#         index = int(((degrees + 22.5) % 360) / 45)
#         return directions[index]


# city_id = get_city_id(city_name)


# weather_api_url_base = 'https://api.gismeteo.net/v2/weather/current/'+str(city_id)+'/'
# weather_response = requests.get(weather_api_url_base, headers=headers)
# weather_data = json.loads(weather_response.content.decode('utf-8'))

# pprint.pprint(weather_data)

# print(f"Сейчас в городе {city_name} такая дата отображения погоды: {weather_data['response']['date']['local']}")

# discription_about_weather = weather_data['response']['description']['full']
# air_temperature = weather_data['response']['temperature']['air']['C']
# water_temperature = weather_data['response']['temperature']['water']['C']
# pressure = weather_data['response']['pressure']['mm_hg_atm']
# humidity = weather_data['response']['humidity']['percent']
# wind_speed = weather_data['response']['wind']['speed']['m_s']
# storm = weather_data['response']['storm']
# osadki = weather_data['response']['precipitation']['type']
# wind_direction = weather_data['response']['wind']['direction']['degree']
# wind_direction_name = get_wind_direction(wind_direction)

# print('Погода в городе', city_name, 'на сегодня:')
# print(f'В целом,погода в городе {city_name} - {discription_about_weather}')
# print('Температура:', air_temperature, 'градусов по Цельсию')
# print(f'Температура воды в вашем городе - {water_temperature}')
# print('Давление:', pressure, 'мм рт. ст.')
# print('Влажность:', humidity, '%')
# print('Скорость ветра:', wind_speed, 'км/ч')
# print('Направление ветра:', wind_direction_name)

# cloud_dict = {
#     0 : 'Ясно',
#     1 : 'Малооблачно',
#     2 : 'Облачно',
#     3 : 'Пасмурно',
#     101 : 'Переменная облачность'
# }

# cloud_type = weather_data['response']['cloudiness']['type']

# if cloud_type in cloud_dict:
#     print('Облачность:', cloud_dict[cloud_type])
# else:
#     print('Тип облачности неизвестен:', cloud_type)

# print(f'Вероятность шторма в городе {city_name} - {storm}')
# weather_intensity_dict = {
#     0: 'Нет осадков',
#     1: 'Небольшой дождь / снег',
#     2: 'Дождь / снег',
#     3: 'Сильный дождь / снег'
# }
# weather_intensity = weather_data['response']['precipitation']['intensity']
# if weather_intensity in weather_intensity_dict:
#     print(f'интенсивность - {weather_intensity_dict[weather_intensity]}')
# else:
#     print('Что то неизвестное')
# # pprint.pprint(get_info_about_city())

# import requests
# from bs4 import BeautifulSoup
    
# url = "https://biblioteka-online.info/book/piraty-ledovogo-morya/reader/216/"
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# quotes = soup.find_all(class_='article_books_cn   ')

# for elem in quotes:
#     print('-'*20)
#     print(elem.text)

import requests
from bs4 import BeautifulSoup

url = 'https://old-album.ru/contacts/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

text = soup.find_all(class_='description')
print(text)


