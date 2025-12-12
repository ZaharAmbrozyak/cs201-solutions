import json

# import requests
# key = "e90fab7014064d2c88795d9fd95afa6f"
# city = input('City>>>')
# link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
# data = eval(requests.get(link).text)

# for k,v in data.items():
#     print(k, v)

filename = 'my_data.json'
with open(filename, 'r') as f:
    data = json.load(f)

forecast = data['main']
coords = data['coord']
city_name = data['name']
weather = data['weather'][0]
wind = data['wind']
deg = wind['deg']
direction = ['N', 'NNW', 'NW', 'NWW',
       'W', 'SWW', 'SW', 'SSW',
       'S', 'SSE', 'SE', 'SEE',
       'E', 'NEE', 'NE', 'NEE']
deg_code = int(round(deg/22.5, 0))%16

print(f"Weather in {city_name}")

print(f"\nTemperature is {int(forecast['temp']-273.15)} Celcius")

print(f"\nWeather situation is {weather['main']}")

print("\nWind situation is:")
print(f"Speed: {wind['speed']}")
print(f"Degree: {deg} degrees")
print(f"Direction: {direction[deg_code]}")

