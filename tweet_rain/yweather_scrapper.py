import yweather
 
class yweather_scraper(NebriOS):
    # https://yweather.readthedocs.org/en/v0.1/intro.html
    listens_to = ['check_city_weather', 'check_country_weather']
 
    def check(self):
        return self.check_city_weather and self.check_country_weather is not None
 
    def action(self):
        # preserve previous weather value
        shared.weather_prev = shared.weather_next
        
        # start getting weather from YWeather 
        client = yweather.Client()
        id = client.fetch_woeid(self.check_city_weather + " " + self.check_country_weather)
        weather_dump = client.fetch_weather(id, metric=True)
        # uncomment for testing purpose, generating KVP
        #self.yweather_action = "Ran"
        
        # which type of weather crawled
        # https://developer.yahoo.com/weather/#codes
        alert_list = ["0","1","2","3","4","11","12","21","24","26","27","28","38","39","40"]
        
        
        if weather_dump["condition"]["code"] in alert_list:
            self.weather_code = weather_dump["condition"]["code"]
            self.weather_text = weather_dump["condition"]["text"]
            self.weather_date = weather_dump["condition"]["date"]
            self.weather_temp = weather_dump["condition"]["temp"]
            shared.weather_next = { 'location': id, 'code': self.weather_code, 'date': self.weather_date }
        
        # for testing purpose:
        '''
        self.weather_code = weather_dump["condition"]["code"]
        self.weather_text = weather_dump["condition"]["text"]
        self.weather_date = weather_dump["condition"]["date"]
        self.weather_temp = weather_dump["condition"]["temp"]
        self.weather_next = { 'location': id, 'code': self.weather_code, 'date': self.weather_date }
        '''
