from pyowm import OWM
import math
API_key = 'c5fed2aabc1ab49b5b1b78ecfb303452'
owm = OWM(API_key)

lat = 49.043091
lon = 41.038962
geolocation = []
print(lon, ' ', lat)
for i in range(0,20):
    observation = owm.weather_at_coords(lon,lat)
    weather = observation.get_weather()
    windVector = dict.get(weather.get_wind(), 'deg')
    windSpeed = dict.get(weather.get_wind(), 'speed')
    if (windSpeed == 'None'):
        break
    lon += windSpeed * math.sin(float(windVector))
    lat += windSpeed * math.cos(float(windVector))
    geolocation.append((lat, lon))
    # print(lon, ' ', lat)


js_code = ""


for loc in geolocation:
    js_code += '{lat: %s, lng: %s},\n' % (loc[0], loc[1])
js_code=js_code[0:-2]
print(js_code)
html = open('points&lines.html')
html = html.replace('/* PLACEHOLDER */', js_code)
f = open('points&lines.html', 'w')
f.write(html)
f.close()