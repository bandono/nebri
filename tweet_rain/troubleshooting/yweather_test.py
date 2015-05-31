import yweather
 
class yweather_test(NebriOS):
    # https://yweather.readthedocs.org/en/v0.1/intro.html
    listens_to = ['test_city_weather', 'test_country_weather']
 
    def check(self):
        return self.test_city_weather and self.test_country_weather is not None
 
    def action(self):
        client = yweather.Client()
        id = client.fetch_woeid(self.test_city_weather + " " + self.test_country_weather)
        weather_dump = client.fetch_weather(id, metric=True)
        # uncomment for testing purpose, generating KVP
        #self.yweather_action = "Ran"
        
        self.weather_code = weather_dump["condition"]["code"]
        self.weather_text = weather_dump["condition"]["text"]
        self.weather_date = weather_dump["condition"]["date"]
        self.weather_temp = weather_dump["condition"]["temp"]
        self.weather_next = { 'location': id, 'code': self.weather_code, 'date': self.weather_date }
        self.weather_prev = self.weather_next
