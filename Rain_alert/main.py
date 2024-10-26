from dotenv import load_dotenv
import requests 
from datetime import datetime
import os




load_dotenv()
API_KEY = os.getenv("Api_key")
print(API_KEY)

def get_data():
    main_url = "http://api.openweathermap.org/data/2.5/find?"
    api_key = API_KEY
    City = "Johannesburg"
    url = main_url + "appid=" + api_key + "&q=" + City
    Data = requests.get(url)
    print(Data.json()['list'][0]['main']['temp'])
   

#still trying to commit 
get_data




get_data()