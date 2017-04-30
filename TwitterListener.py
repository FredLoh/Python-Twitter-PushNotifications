import tweepy

from Authentication import Authentication
from pyfcm import FCMNotification


class TwitterStreamListener(tweepy.StreamListener):
    push_service = FCMNotification(api_key=Authentication.firebase_auth_key())

    def on_status(self, status):
        registration_ids = Authentication.firebase_registration_ids()
        message_title = "Support Alert"
        message_body = status.text

        message_data = {
            "link": "https://twitter.com/statuses/" + str(status.id),
            "alternative_link": "http://twitter.com/none/status/" + str(status.id)
        }
        self.push_service.notify_multiple_devices(registration_ids=registration_ids,
                                                  message_title=message_title,
                                                  message_body=message_body,
                                                  data_message=message_data)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False
