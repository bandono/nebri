import twitter

class pytwitter_auth(NebriOS):
    listens_to = ['shared.ttoken', 'shared.ttoken_secret', 'shared.tconsumer_key', 'shared.tconsumer_secret', 'tcode']

    def check(self):
        return self.tcode

    def action(self):
        auth = twitter.OAuth(shared.ttoken, shared.ttoken_secret, shared.tconsumer_key, shared.tconsumer_secret)
        t = twitter.Twitter(auth=auth)
        try:
            t.account.verify_credentials()
            self.pytwitter_auth = "Ran"
        except:
            self.pytwitter_auth = "Fail"
