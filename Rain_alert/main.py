import requests,json
from datetime import datetime
def get_data():
    main_url = "http://api.openweathermap.org/data/2.5/find?"
    api_key = "a62b27850143efeed1afbd419aff0078"
    City = "Johannesburg"
    url = main_url + "appid=" + api_key +"&q=" + City
    Data = requests.get(url).json()
    print(Data)

get_data()