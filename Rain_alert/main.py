from twilio.rest import Client
import os
from dotenv import load_dotenv
import requests 




load_dotenv()
API_KEY = os.getenv("Api_key")
   
main_url = "http://api.openweathermap.org/data/2.5/find?"
api_key = API_KEY
City = "Cape Town"
url = main_url + "appid=" + api_key + "&q=" + City

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
Data = requests.get(url)
Data = Data.json()


def rain_check():
    weather_conditions = Data["list"][0]
    print(weather_conditions)
    if any(condition in ["rain"] for condition in weather_conditions):
        send_alert()
    else:
        print("No rain expected!")
        
        
def send_alert():
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body = "Alert: Please be aware that rain is expected today!!,Do not forget your umbrella (-_-)",
    from_='+12092850985',
    to='+27652515201'
    )
    print("Alert_rain",message.sid)




rain_check()