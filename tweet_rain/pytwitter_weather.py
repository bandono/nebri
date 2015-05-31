import twitter

class pytwitter_weather(NebriOS):
    listens_to = ['weather_date']
    # tcode is not running yet
    #listens_to = ['weather_next', 'tcode']

    def check(self):
        '''try:
            # check whether we're comparing a same location from last check
            if shared.weather_next["location"] == shared.weather_prev["location"]:
                # check whether for this same location weather information
                # hasn't changed (by checking last check code
                
                # debug purpose:
                self.wlocdiff = True
                try:
                    if shared.weather_next["code"] != shared.weather_prev["code"]:
                        checkFlag = True
                        
                        # debug purpose:
                        self.wcodediff = True 
                    else:
                        #checkFlag = False
                        # for checking purpose if weather code actually remain
                        # the same as before e.g. it's been "Cloudy" for long:
                        checkFlag = True
                except:
                    checkFlag = True
            # if not comparing same location, skip checking just proceed as True
            else:
                checkFlag = True
        except:
            checkFlag = True

        # tcode is not running
        #return self.tcode or checkFlag
        return checkFlag'''
        return True

        
    def action(self):
        # update previous weather key:
        #self.weather_prev = self.weather_next
        
        auth = twitter.OAuth(shared.ttoken, shared.ttoken_secret, shared.tconsumer_key, shared.tconsumer_secret)
        t = twitter.Twitter(auth=auth)
        status = self.check_city_weather + " is " + self.weather_text + " with temperature at "+ self.weather_temp + " °C. Taken at " + self.weather_date
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
