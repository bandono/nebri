import twitter

class pytwitter_forecast(NebriOS):
    listens_to = ['forecast_date']


    def check(self):
        return True

        
    def action(self):        
        auth = twitter.OAuth(shared.ttoken, shared.ttoken_secret, shared.tconsumer_key, shared.tconsumer_secret)
        t = twitter.Twitter(auth=auth)
        status = "Forecast: " + self.check_city_forecast + " is " + self.forecast_text + " with temperature "+ self.forecast_lo + " - " + self.forecast_hi + " °C for " + self.forecast_date
        try:
            t.account.verify_credentials()
            try:
                t.statuses.update(status=status)
                # uncomment to update KVP of auth status for checking
                #self.pytwitter_update = "Run"
            except:
                self.pytwitter_update = "Fail"
        except:
            self.pytwitter_auth = "Fail"
