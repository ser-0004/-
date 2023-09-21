import requests
city = 'Moscow'
appid = '547041d29f8c2f842fdba37eb889c88d'
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура:", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'], 'м/с')
print("Видимость:", data['visibility'], 'm')
print("____________________________")
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата", i['dt_txt'], "\r\nТемпература", format(i['main']['temp']), " \r\nПогодные условия ", i['weather'][0]['description'], "\r\nCкорость ветра:", i['wind']['speed'], 'м/с'
          , "\r\nВидимость:", i['visibility'], 'm')
    print("____________________________")