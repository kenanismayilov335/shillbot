from telethon import TelegramClient
import sys
import time
import datetime

starttime = time.time()

#H3T MAN
api_id = 13811273
api_hash = '03c686397abdcb6124880ab8f6de7595'
message_here = '''⭐Launch: 17.00  UTC
🟢Starting liqudity 0.3bnb 
🟢Liquidity Lock 3days
🟢Real Community
🟢Liquidity locked immediately post launch 

° Telegram : @mysterylaunch101
--------------------------------------------'''


groups = ['@safeanalyzershill', '@bezoscallsdiscussionn','@hitmansdiscussion','@Comet_Calls_Chat','@DeveloperHubBSC']

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
    time.sleep(30 - ((time.time() - starttime) % 1))

