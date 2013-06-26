from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import xlwt
from datetime import datetime

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="07gYM9jld3vmqb4aaFE2uQ"
consumer_secret="inNjbu0NJFZ4e0Q83aVC0PxDgnHnon35MamOKU5N3w"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1543347734-FlLNOb7a92WCbfWCANLj5M9RKd2j59vTzzVqwbX"
access_token_secret="nZ2Cpic5cnAxI6FcjQYmRbIc77jHWlUWCS2WAD4qg"

number_id = 1
number_save = 0
page_number = 1
excel_max = 1000
style1 = xlwt.easyxf('font: name Times New Roman, colour black')
style2 = xlwt.easyxf('font: name Times New Roman, colour white, bold on')
style2 = xlwt.easyxf('pattern: back_colour black')
wb = xlwt.Workbook()
ws = wb.add_sheet('Hoja 1',cell_overwrite_ok=True)

def start_data():
    global ws
    print 'start_data'
    ws.write(0,0, 'contributors', style1)
    ws.write(0,1, 'coordinates', style1)
    ws.write(0,2, 'created_at', style1)
    ws.write(0,3, 'favorite_count', style1)
    ws.write(0,4, 'favorited', style2)
    ws.write(0,5, 'filter_level', style2)
    ws.write(0,6, 'id', style2)
    ws.write(0,7, 'in_reply_to_screen_name', style2)
    ws.write(0,8, 'in_reply_to_status_id', style2)
    ws.write(0,9, 'in_reply_to_status_id_str', style2)
    ws.write(0,10, 'in_reply_to_user_id', style2)
    ws.write(0,11, 'in_reply_to_user_id_str', style2)
    ws.write(0,12, 'place', style2)
    ws.write(0,13, 'retweet_count', style2)
    ws.write(0,14, 'retweeted', style2)
    ws.write(0,15, 'lang', style1)
    ws.write(0,16, 'id', style1)
    ws.write(0,17, 'id_str', style1)
    ws.write(0,18, 'name', style1)
    ws.write(0,19, 'followers_count', style1)
    ws.write(0,20, 'friends_count', style1)
    ws.write(0,21, 'time_zone', style1)
    ws.write(0,22, 'hashtags', style1)
    ws.write(0,23, 'urls', style1)
    ws.write(0,24, 'user_mentions', style1)
        

    
    wb.save('Data'+ str(datetime.now().strftime("%Y-%m-%d")) +'.xls')

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """


        
    def on_data(self, data):
        global number_save, number_id, page_number, ws
        myJson = json.loads(data)
        ws.write(number_id,0, myJson['contributors'], style1)
        ws.write(number_id,1, str(myJson['coordinates']), style1)
        ws.write(number_id,2, myJson['created_at'], style1)
        ws.write(number_id,3, myJson['favorite_count'], style1)
        ws.write(number_id,4, myJson['favorited'], style1)
        ws.write(number_id,5, myJson['filter_level'], style1)
        ws.write(number_id,6, myJson['id'], style1)
        ws.write(number_id,7, myJson['in_reply_to_screen_name'], style1)
        ws.write(number_id,8, myJson['in_reply_to_status_id'], style1)
        ws.write(number_id,9, myJson['in_reply_to_status_id_str'], style1)
        ws.write(number_id,10, myJson['in_reply_to_user_id'], style1)
        ws.write(number_id,11, myJson['in_reply_to_user_id_str'], style1)
        ws.write(number_id,12, str(myJson['place']), style1)
        ws.write(number_id,13, myJson['retweet_count'], style1)
        ws.write(number_id,14, myJson['retweeted'], style1)
        ws.write(number_id,15, myJson['lang'], style1)
        ws.write(number_id,16, myJson['user']['id'], style1)
        ws.write(number_id,17, myJson['user']['id_str'], style1)
        ws.write(number_id,18, myJson['user']['name'], style1)
        ws.write(number_id,19, myJson['user']['followers_count'], style1)
        ws.write(number_id,20, myJson['user']['friends_count'], style1)
        ws.write(number_id,21, myJson['user']['time_zone'], style1)
        ws.write(number_id,22, str(myJson['entities']['hashtags']), style1)
        ws.write(number_id,23, str(myJson['entities']['urls']), style1)
        ws.write(number_id,24, str(myJson['entities']['user_mentions']), style1)
        
        
        print data
        print myJson['text']
        number_id+=1
        if(number_save > 10):
            wb.save('Data'+ str(datetime.now().strftime("%Y-%m-%d")) +'.xls')
            print "Save"
            number_save = 0
        else:
            number_save+=1
        if(number_id >= excel_max):
            page_number+=1
            number_id = 0
            ws = wb.add_sheet('Hoja '+ str(page_number),cell_overwrite_ok=True)
        return True

    def on_error(self, status):
        print status

 


if __name__ == '__main__':
    start_data()
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['El Paro , Parados, Sin trabajo'])
