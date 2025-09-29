import requests
API_KEY = "2c9464d0e5cc0595f288cb86a661cf4d"

location_res = requests.get('https://ipinfo.io/json')
location_data = location_res.json()
city = location_data.get('city')

weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
weather_res = requests.get(weather_url)


print(f"Weather in {city}: {weather_res}")