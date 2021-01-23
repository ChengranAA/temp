import requests
import geoip2.database

def getWeather():

    # find local city name
    IP_address = requests.get('http://ifconfig.me/ip', timeout=1).text.strip()
    reader = geoip2.database.Reader("/Users/andrewli/myscript/weather_message/GeoLite2-City_20210122/GeoLite2-City.mmdb")
            ## change this directory to your working directory

    response = reader.city(IP_address)
    city_name_cn = response.city.names['zh-CN']
    city_name_en = response.city.names['en']

    country_iso_code = response.country.iso_code

    city = city_name_en+ "," + country_iso_code

    # get weather from openweathermap
    api_key = "c8affe8b08c4b2d249ca470d358f8925"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        # temperature and humidity
        current_temperature = str(int(int(y["temp"]) - 273.15))
        current_humidiy = y["humidity"]

        z = x["weather"]

        # description of weather
        weather_description = z[0]["description"]

    else:
        print("Sorry, i can't find the weather of your %s" %(city_name_en))

    return [city_name_en, current_humidiy, current_temperature, weather_description]
