from telethon import TelegramClient
import sys
import time
import datetime

starttime = time.time()

#H3T MAN
api_id = 13811273
api_hash = '03c686397abdcb6124880ab8f6de7595'
message_here = '''0x4cece4036881f866182c5b5ee26d0a4a6ff9bc82
'''


groups = ['@TM_ScamFuckerGlobal','@TM_ScamFucker','@Pink_ChaHeYue','@neverscamagain']

failcount = 0;
 
while True:
    with TelegramClient('anon', api_id, api_hash) as client:
        for x in groups:
            try:
                client.loop.run_until_complete(client.send_message (x, message_here))
            
            
            
            except:
                print(x, sys.exc_info()[0])
                failcount += 1
    print(datetime.datetime.now(), str(failcount/len(groups) * 100) + '%')
    time.sleep(60 - ((time.time() - starttime) % 1))
    