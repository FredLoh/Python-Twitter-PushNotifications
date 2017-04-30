import tweepy
from TwitterListener import TwitterStreamListener
from Authentication import Authentication


def main():
    # Replace with words you wish to search for.
    key_words = ['']

    api = Authentication.create_twitter_auth_object()

    twitter_stream = tweepy.Stream(auth=api.auth, listener=TwitterStreamListener())
    twitter_stream.filter(track=key_words)

if __name__ == "__main__":
    main()




