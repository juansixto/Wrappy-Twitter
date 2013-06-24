from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="07gYM9jld3vmqb4aaFE2uQ"
consumer_secret="inNjbu0NJFZ4e0Q83aVC0PxDgnHnon35MamOKU5N3w"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1543347734-FlLNOb7a92WCbfWCANLj5M9RKd2j59vTzzVqwbX"
access_token_secret="nZ2Cpic5cnAxI6FcjQYmRbIc77jHWlUWCS2WAD4qg"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        myJson = json.loads(data)
        print myJson['created_at'] + "    " +myJson['user']['name'] + ' : ' + myJson['text']
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Chelsea'])
