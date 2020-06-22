import requests
import bs4
import json

#This function helps to send weather details at timed interval to slack channel using the timer.py file


def timer():
    slack_token = ''  #get the slack token value you intend to use and substitute
    slack_channel = '#tunmmy'
    slack_icon_url = "https://i.ibb.co/KVY5wMV/rr.png" 
    slack_user_name = 'Weather Reports'

    try:

        def slack_weather(place):
            #The str(place) in the url makes the value dynamic,substitute for the return value of place in def slack_weather
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

            visibility =weather['visibility']
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



            text = 'for today we have longitude *{}* and latitude *{}* for this weather with id *{}*,main *{}*,description *{}*,icon *{}* and base *{}*temperature *{}* that feelslike *{}* the minimum temp is *{}* and maximum is *{}* ,with pressure *{}* and *{}* humidity.'.format(lon,lat,id_,main,description,
            icon,base,main,feels_like,temp_min,temp_max,pressure,humidity)



            # text = 'for today we have longitude*{}* and latitude *{}* for this weather with id*{}*,main*{}*,description*{},icon*{}* and base*{}*temperature*{}* that feelslike*{}* the minimum temp is *{}* and maximum is *{}*
            #  ,with pressure*{}* and *{}* humidity'.format(lon,lat,id_,main,description,icon,base,main,feels_like,temp_min,temp_max)'
                    
                    
            return requests.post('https://slack.com/api/chat.postMessage', {
                'token': slack_token,
                'channel': slack_channel,
                'text': text,
                'icon_url': slack_icon_url,
                'username': slack_user_name
                #'blocks': json.dumps(blocks) if blocks else None
            }).json()	
    except:
        pass


    #This is the value of place in the url
    location = "abuja"
    #location here is the returning value of the function above which is place
    slack_weather(location)
