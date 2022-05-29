from telethon import TelegramClient
import sys
import time
import datetime

starttime = time.time()

#rogi roe
api_id = 11362963
api_hash = '02bb1a6fdeea5b719818db93156a89ad'
message_here = open("shilllpost.txt")
kazim = message_here.readline()

groups = ['@crypt0news2021', '@cryptolinksgroup', '@cryptolinks2020', '@cryptooo10', '@cryptoworld2024', '@exchangecity2020', '@tradersgr0up', '@bull2020bear', '@Trustedpr0ject', '@informationtoken', '@stockmarket2024', '@databl0ckchain', '@investments2022', '@bl0ckchainnews', '@communityaltcoin', '@poocoinshill', '@goshitcoins', '@CRYPTOMOONHOT', '@BSCBombers', '@BSCGemsENG', '@CryptoFamilyGroup', '@CryptoM00NShots', '@dexgemschat', '@to2themoonn', '@uniswaplegit', '@UniswapInvestorssss', '@uniswaprektplebs', '@whalers_club', '@xxxxxx1000000', '@whaler_club', '@uniswap_talk', '@bscgems247', '@CoinhuntCC', '@uniswapw', '@jumpsquad', '@uniswapall', '@uniswapbombsgroup', '@defiandmore', '@uniswapgem123', '@KCC_Lovers', '@EliteCryptoShillers', '@RoseEnglishSignal', '@bscmoonz', '@uniswaptrollbox', '@MoonUrBSCtoken', '@UniswapGemGroup', '@bscmoon', '@UniswapObserver', '@DeFiPresales', '@chatbsc', '@cryptolux_tl', '@memeszn', '@ShillUSA', '@lauragem', '@bsc_moonshots', '@Defi_shill', '@GoodFellas_Cryptopicks', '@apeslounge', '@BscGemGlobal',]

failcount = 0;
 
while True:
    with TelegramClient('anon', api_id, api_hash) as client:
        for x in groups:
            try:
                client.loop.run_until_complete(client.send_message (x, kazim))
            
            
            
            except:
                print(x, sys.exc_info()[0])
                failcount += 1
    print(datetime.datetime.now(), str(failcount/len(groups) * 100) + '%')
    time.sleep(120 - ((time.time() - starttime) % 1))

