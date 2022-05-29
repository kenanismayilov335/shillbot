from telethon import TelegramClient
import sys
import time
import datetime

starttime = time.time()

#H3T MAN
api_id = 13886510
api_hash = 'bb0ff72809482dc9a696f3856e90c9a9'
message_here = ''''''


groups = ['@defiandmore', '@uniswapgem123', '@KCC_Lovers', '@EliteCryptoShillers', '@RoseEnglishSignal', '@bscmoonz', '@uniswaptrollbox', '@MoonUrBSCtoken', '@UniswapGemGroup', '@bscmoon', '@UniswapObserver', '@DeFiPresales', '@chatbsc', '@cryptolux_tl', '@memeszn', '@ShillUSA', '@lauragem', '@bsc_moonshots', '@Defi_shill', '@GoodFellas_Cryptopicks', '@apeslounge', '@BscGemGlobal',]

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

