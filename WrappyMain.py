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

number_id = 0
number_save = 0
page_number = 1
excel_max = 1000

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    style0 = xlwt.easyxf('font: name Times New Roman, colour black, bold on')
    style1 = xlwt.easyxf('',num_format_str='DD-MMM-YY')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Hoja 1',cell_overwrite_ok=True)
    
    def on_data(self, data):
        global number_save, number_id, page_number, ws
        myJson = json.loads(data)
        print myJson['created_at'] + "    " +myJson['user']['name'] + ' : ' + myJson['text']
        ws.write(number_id,0, myJson['created_at'], style1)
        ws.write(number_id,1, myJson['user']['name'], style1)
        ws.write(number_id,2, myJson['text'], style1)
        number_id+=1
        if(number_id >= excel_max):
            page_number+=1
            number_id = 0
            ws = wb.add_sheet('Hoja '+ str(page_number),cell_overwrite_ok=True)            
            
        
        if(number_save > 10):
            wb.save('Data'+ str(datetime.now().strftime("%Y-%m-%d")) +'.xls')
            number_save = 0
        else:
            number_save+=1
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['El Paro , Parados, Sin trabajo'])
