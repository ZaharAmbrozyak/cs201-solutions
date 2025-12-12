import requests

dir1 = ('N', 'W', 'S', 'E')
dir2 = ('N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE')
dir3 = ('N', 'NNW', 'NW', 'NWW',
       'W', 'SWW', 'SW', 'SSW',
       'S', 'SSE', 'SE', 'SEE',
       'E', 'NEE', 'NE', 'NEE')
precisions = {
    'low': (4, dir1),
    'medium': (8, dir2),
    'high': (16, dir3)
}
def get_info(city):
    key = "e90fab7014064d2c88795d9fd95afa6f"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    output = eval(requests.get(link).text)
    return output

data = get_info(input("Введіть назву міста: "))

def get_name(data):
    return data['name']

def get_weather(data):
    return data['weather'][0]['main']

def get_temperature(data, type):
    T_CONST = 273.15
    if type == "C":
        return int(data['main']['temp']-T_CONST)
    elif type == 'F':
        return int(data['main']['temp']-T_CONST)*9/5 + 32
    return int(data['main']['temp'])

def get_wind_speed(data):
    return data['wind']['speed']

def get_degree(data):
    return data['wind']['deg']

def get_direction(precision):
    n_sec, directions = precisions[precision]
    deg_sec = 360/n_sec
    return directions[int(round(degree/deg_sec, 0))%n_sec]

city_name = get_name(data)
temp_type = input("Введіть систему температури (C/F/K):").upper()
temperature = get_temperature(data, 'C')
weather_situation = get_weather(data)
wind_speed = get_wind_speed(data)
degree = get_degree(data)

precision = input("Введіть точність (low, medium, high): ").lower()
direction = get_direction(precision)

print(f"Weather in {city_name}:")
print(f"\nTemperature is {temperature} {temp_type}")
print(f"\nWeather situation: {weather_situation}")
print(f"\nWind speed: {wind_speed}")
print(f"Direction: {direction}")

