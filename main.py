from telethon import TelegramClient
import sys
import time
import datetime

starttime = time.time()

#H3T MAN
api_id = 11362963
api_hash = '02bb1a6fdeea5b719818db93156a89ad'
message_here = '''⭐️ 𝐗-𝐌𝐄𝐍 𝐌𝐀𝐑𝐊𝐄𝐓𝐈𝐍𝐆 𝐒𝐄𝐑𝐕𝐈𝐂𝐄𝐒 ⭐️

--------------------------------------------

🚨𝗦𝗛𝗜𝗟𝗟𝗜𝗡𝗚 𝗦𝗘𝗥𝗩𝗜𝗖𝗘𝗦:

𝗪𝗲 𝗰𝗮𝗻 𝗦𝗛𝗜𝗟𝗟 𝘂𝗿 𝗽𝗿𝗼𝗷𝗲𝗰𝘁 𝗼𝗻 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗮𝗻𝗱 𝘁𝘄𝗶𝘁𝘁𝗲𝗿 𝘄𝗶𝘁𝗵 𝗻𝗼𝗻 𝘀𝘁𝗼𝗽❟ 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗴𝗲𝘁 𝟯𝟬𝟬 - 𝟰𝟬𝟬 𝗜𝗡𝗩𝗘𝗦𝗧𝗘𝗥𝗦

☎️SHILLING CONTACT: @kazimbasha

--------------------------------------------

🚨𝗨𝗣𝗩𝗢𝗧𝗘𝗦 𝗦𝗘𝗥𝗩𝗜𝗖𝗘𝗦:

𝗪𝗲 𝗰𝗮𝗻 𝗺𝗮𝗸𝗲 𝗮𝗹𝗹 𝘀𝗶𝘁𝗲𝘀 𝗨𝗣𝗩𝗢𝗧𝗘𝗦❟ 𝗹𝗶𝗸𝗲 𝗖𝗢𝗜𝗡𝗦𝗡𝗜𝗣𝗘𝗥❟ 𝗖𝗢𝗜𝗡𝗦𝗖𝗢𝗣𝗘❟ 𝗖𝗢𝗜𝗡𝗠𝗢𝗢𝗡𝗘𝗥❟ 𝗪𝗔𝗧𝗖𝗛𝗘𝗥𝗚𝗨𝗥𝗨❟ 𝗮𝗻𝗱 𝗺𝗼𝗿𝗲 𝗲𝘁𝗰｡｡｡｡

☎️UPVOTES CONTACT: @kazimbasha

--------------------------------------------

🚨𝗪𝗔𝗧𝗖𝗛𝗟𝗜𝗦𝗧𝗦 𝗦𝗘𝗥𝗩𝗜𝗖𝗘𝗦:

𝗪𝗲 𝗰𝗮𝗻 𝗺𝗮𝗸𝗲 𝘄𝗮𝘁𝗰𝗵𝗹𝗶𝘀𝘁𝘀 𝗼𝗻 𝗖𝗢𝗜𝗡𝗠𝗔𝗥𝗞𝗘𝗧𝗖𝗔𝗣 𝗮𝗻𝗱 𝗖𝗢𝗜𝗡𝗚𝗘𝗖𝗞𝗢 ( 𝗳𝗮𝘀𝘁 𝗮𝗻𝗱 𝘀𝗲𝗰𝘂𝗿𝗲 )

☎️ WATCHLISTS CONTACT: @kazimbasha

--------------------------------------------

🚨𝗢𝗧𝗛𝗘𝗥 𝗦𝗘𝗥𝗩𝗜𝗖𝗘𝗦:

𝟭｡ 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴𝘀 𝗼𝗻 𝗗𝗲𝘅𝘁𝗼𝗼𝗹𝘀❟ 𝗽𝗶𝗻𝗸𝘀𝗮𝗹𝗲

𝟮｡ 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝘀𝘁𝗶𝗰𝗸𝗲𝗿𝘀❟ 𝗯𝗮𝗻𝗻𝗲𝗿𝘀❟ 𝗹𝗼𝗴𝗼𝘀

𝟯｡ 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗯𝗼𝘁𝘀❟ 𝗿𝗲𝗳𝗳𝗲𝗿𝗮𝗹𝘀 𝗯𝗼𝘁𝘀 𝗮𝗻𝗱 𝗲𝘁𝗰｡

𝟰｡ 𝗪𝗲𝗯 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗺𝗲𝗻𝘁｡ ( 𝗟𝗼𝘄 𝗽𝗿𝗶𝗰𝗲𝘀 )

--------------------------------------------

☎️CONTACT : @kazimbasha

☎️CONTACT : @kazimbasha

☎️CONTACT : @kazimbasha

--------------------------------------------'''


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

