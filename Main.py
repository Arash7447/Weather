from Base import WeatherAPIBase

import requests

class OpenMeteo(WeatherAPIBase):
    
    def __init__(self,latitude ,longitude,**kwargs):
        
        self.latitude = latitude
        self.longitude = longitude
    
    def get_current_temperature(self):

        params = {"latitude":self.latitude ,"longitude":self.longitude , "current_weather":True}

        result = requests.get("https://api.open-meteo.com/v1/forecast" , params = params)

        result_json = result.json()

        return result_json["current_weather"]["temperature"]


class OpenWeather(WeatherAPIBase):
    
    def __init__(self,latitude ,longitude,**kwargs):
        self.latitude = latitude
        self.longitude = longitude    
        self.api_token = kwargs.get("api_token")  

    def get_current_temperature(self):

        params = {"lat":self.latitude ,"lon":self.longitude , "appid":self.api_token}

        result = requests.get("https://api.openweathermap.org/data/2.5/weather" , params = params)

        result_json = result.json()

        
        return result_json["main"]["temp"] -273.15
   






if __name__ == "__main__" :

    open_meteo_obj = OpenMeteo(35.69,51.42)
    print(open_meteo_obj.get_current_temperature())


    open_weather_obj = OpenWeather(35.69,51.42,api_token = "daa509c8e8c0091f7c7c1b645f94a3e9")
    print(open_weather_obj.get_current_temperature())