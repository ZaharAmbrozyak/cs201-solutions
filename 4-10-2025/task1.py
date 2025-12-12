import json

filename = 'my_data.json'
with open(filename, 'r') as f:
    data = json.load(f)

directions = ['N', 'NNW', 'NW', 'NWW',
       'W', 'SWW', 'SW', 'SSW',
       'S', 'SSE', 'SE', 'SEE',
       'E', 'NEE', 'NE', 'NEE']

N_SEC = 16
T_CONST = 273.15
DEG_SEC = 360/N_SEC

city_name = data['name']
temperature = int(data['main']['temp']-T_CONST)
weather_situation = data['weather'][0]['main']
wind_speed = data['wind']['speed']
degree = data['wind']['deg']
direction = directions[int(round(degree/DEG_SEC, 0))%N_SEC]

print(f"Weather in {city_name}:")
print(f"\nTemperature is {temperature} celsius")
print(f"\nWeather situation: {weather_situation}")
print(f"\nWind speed: {wind_speed}")
print(f"Direction: {direction}")

