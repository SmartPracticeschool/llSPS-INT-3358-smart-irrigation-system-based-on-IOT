import requests

api_address='http://api.openweathermap.org/data/2.5/weather?&appid=64b2cf5d5192425f590439bd8ef54d7d&q='
city=input("city name :")

url = api_address + city

json_data = requests.get(url).json()

print(json_data)
