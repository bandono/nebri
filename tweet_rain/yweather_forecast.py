import yweather
 
class yweather_forecast(NebriOS):
    # https://yweather.readthedocs.org/en/v0.1/intro.html
    listens_to = ['check_city_forecast', 'check_country_forecast']
 
    def check(self):
        return self.check_city_forecast and self.check_country_forecast is not None
 
    def action(self):       
        # start getting weather from YWeather 
        client = yweather.Client()
        id = client.fetch_woeid(self.check_city_forecast + " " + self.check_country_forecast)
        weather_dump = client.fetch_weather(id, metric=True)
        # uncomment for testing purpose, generating KVP
        #self.yweather_action = "Ran"
        
        self.forecast_text = weather_dump["forecast"][0]["text"]       
        self.forecast_lo = weather_dump["forecast"][0]["low"]
        self.forecast_hi = weather_dump["forecast"][0]["high"]
        self.forecast_date = weather_dump["forecast"][0]["date"]
