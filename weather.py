import requests
import bs4

def weather(place):
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + str(place) + "&appid=2e618abe31ab83e46541fab23cbed2a1"

    response = requests.get(url)
    weather = response.json()
    print(response.text)
    weather_details =(weather['coord']['lon'])
    lon =(weather['coord']['lon'])
    lat = (weather['coord']['lat'])
    # from weather['weather'])
    id_ =(weather['weather'][0]['id'])
    main =(weather['weather'][0]['main'])
    description =(weather['weather'][0]['description'])
    icon =(weather['weather'][0]['icon'])
    print(id_)
    print(main)
    print(description)
    print(icon)
    base = (weather['base'])
    print(base)
    # from main
    main =(weather['main']['temp'])
    print(main)
    feels_like =(weather['main']['feels_like'])
    print(feels_like)
    temp_min =(weather['main']['temp_min'])
    print(temp_min)
    temp_max =(weather['main']['temp_max'])
    print(temp_max)
    pressure =(weather['main']['pressure'])
    print(pressure)
    humidity =weather['main']['humidity']
    print(humidity)

    visibility =(weather['visibility'])
    print(visibility)
    #wind
    wind = (weather['wind']['speed'])
    print(wind)
    deg = (weather['wind']['deg'])
    print(deg)
    #cloud
    clouds = (weather['clouds']['all'])
    print(clouds)

    dt = (weather['dt'])
    print(dt)

    #sys
    sys = (weather['sys']['type'])
    print(sys)
    id__ = (weather['sys']['id'])
    print(id__)
    country = (weather['sys']['country'])
    print(country)
    sunrise = (weather['sys']['sunrise'])
    print(sunrise)
    sunset = (weather['sys']['sunset'])
    print(sunset)
    type_ = (weather['sys']['type'])
    print(type_)

    timezone = weather['timezone']
    id_ = weather['id']
    name = weather['name']
    cod = weather['cod']
    print(id_)
    print(timezone)
    print(name)
    print(cod)

location = "abuja"
weather(location)
