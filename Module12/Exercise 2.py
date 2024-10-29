import requests
import json
class Weather_Forcast:
    def __init__(self,url,location):
        self.url = url
        self.weather_location = location
        self.weather_country = None
        self.weather_time = None
        self.weather_temp = None
        self.weather_condition = None
        self.weather_wind = None
        self.weather_humidity = None
        self.weather_feelslike = None
        self.weather_uv = None

    def weather_search(self):
        params = {
            'key': '60c9c688a405424a913163013242910',
            'q': self.weather_location,
            'aqi':'no'
        }
        try:
            response = requests.get(self.url,params=params)
            response.raise_for_status()
            forecast = response.json()
            #format_forecast = json.dumps(forecast,indent=4)
            self.weather_location = forecast['location']['name']
            self.weather_country = forecast['location']['country']
            self.weather_time = forecast['current']['last_updated']
            self.weather_temp = forecast['current']['temp_c']
            self.weather_condition = forecast['current']['condition']['text']
            self.weather_wind = forecast['current']['wind_mph']
            self.weather_humidity = forecast['current']['humidity']
            self.weather_feelslike = forecast['current']['feelslike_c']
            self.weather_uv = forecast['current']['uv']
            return self.weather_location,self.weather_country,self.weather_time,self.weather_temp,self.weather_condition,self.weather_wind,self.weather_humidity,self.weather_feelslike,self.weather_uv
        except Exception as err:
            print(f"An error occurred: {err}")

    def format_weather(self):
        title_text = 'Weather forecast for '
        title_width = len(title_text)+len(self.weather_location)+len(self.weather_country)+2
        print(f"{'-'*title_width}")
        print(f"{title_text}{self.weather_location}, {self.weather_country}")
        print(f"{'-' * title_width}")
        weather_infor = [
            ('🕑Local Time', self.weather_time),
            ('🌡️Temperature', f'{self.weather_temp} ℃'),
            ('☁️Condition', self.weather_condition),
            ('🍃Wind', f'{self.weather_wind} mph'),
            ('💧Humidity', f'{self.weather_humidity} %'),
            ('👕Feels Like', f'{self.weather_feelslike} ℃'),
            ('🏖️UV', self.weather_uv)]
        for infor_name, infor in weather_infor:
            print(f"{infor_name}: {infor}")
        print(f"{'-' * title_width}")

def main():
    weather_api = f"http://api.weatherapi.com/v1/current.json?"

    while True:
        print("Weather forecast, which city do you want to check?")
        location_input = input("")
        try:
            if location_input =="":
                break
            target_weather = Weather_Forcast(weather_api,location_input)
            target_weather.weather_search()
            target_weather.format_weather()
        except TypeError:
            print(f"Invalid location, please try again")

if __name__ == "__main__":
    main()
