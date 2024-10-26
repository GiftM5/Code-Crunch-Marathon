from twilio.rest import Client
import os
from dotenv import load_dotenv
import requests 




load_dotenv()
API_KEY = os.getenv("Api_key")
    
main_url = "http://api.openweathermap.org/data/2.5/find?"
api_key = API_KEY
City = "Johannesburg"
url = main_url + "appid=" + api_key + "&q=" + City

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
    
def rain_check():
    Data = requests.get(url)
    Data = Data.json()
    
    if Data.status_code == 200:
        weather_conditions = Data["main"]
        rain_expected = any("rain" in condition["main"].lower() for condition in weather_conditions)
        
        if rain_expected:
            send_alert()
        else:
            print("NO RAIN EXPECTED!")
    else:
        print(Data.get("message")) 

def send_alert():
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body = "Alert: Please be aware that rain is expected today!!,Do not forget your umbrella (-_-)",
    from_='+12092850985',
    to='+270652515201'
    )
    print("Alert_rain",message.sid)




if __name__ == "main":
    rain_check()