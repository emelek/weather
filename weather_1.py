from pyowm import OWM

API_key = 'c5fed2aabc1ab49b5b1b78ecfb303452'
print ('API_key =',API_key)
owm = OWM(API_key)

file = open('wind.txt','w')

lon =0
for i in range(-90,90):
    lon = i
    lat = 0
    for j in range(-180,180):
        lat = j
        observation = owm.weather_at_coords(lon,lat)
        weather = observation.get_weather()
        location = observation.get_location()
        windVector = dict.get(weather.get_wind(), 'deg')
        windSpeed = dict.get(weather.get_wind(), 'speed')

        try:
            if windVector <= 22.5:
                windDirection = 'северный'
            elif windVector <= 67.5:
                windDirection = 'северо-восточный'
            elif windVector <= 112.5:
                windDirection = 'восточный'
            elif windVector <= 157.5:
                windDirection = 'юго-восточный'
            elif windVector <= 202.5:
                windDirection = 'южный'
            elif windVector <= 247.5:
                windDirection = 'юго-западный'
            elif windVector <= 292.5:
                windDirection = 'западный'
            elif windVector <= 337.5:
                windDirection = 'северо-западный'
            else:
                windDirection = 'северный'
        except:
            windDirection = 'Штиль'
            windSpeed = 0

        file.write(str(lon) + ' ' + str(lat) + ' ' + windDirection + ' ' + str(windSpeed) + '\n')
        print(lon, ' - ', lat, ' ', windDirection, ' ', windSpeed)


file.close()