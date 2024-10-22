 
import requests,json
from datetime import datetime
import os
from dotenv import load_dotenv



load_dotenv()
API_KEY = os.getenv("API_KEY")
print(API_KEY)

def get_data():
    main_url = "http://api.openweathermap.org/data/2.5/find?"
    api_key = API_KEY
    City = "Johannesburg"
    url = main_url + "appid=" + api_key +"&q=" + City
    Data = requests.get(url)
    print(Data.json()['list'][0]['main']['temp'])
    save_json(Data.json())



def save_json(data):
    with open("data.json","w") as f:
        json.dump(data,f,indent=2)



# get_data()