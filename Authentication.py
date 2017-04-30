import tweepy


class Authentication:
    def __init__(self):
        pass

    @staticmethod
    def create_twitter_auth_object():
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        return tweepy.API(auth)

    @staticmethod
    def firebase_auth_key():
        return ""

    @staticmethod
    def firebase_registration_ids():
        return [
            ""
        ]