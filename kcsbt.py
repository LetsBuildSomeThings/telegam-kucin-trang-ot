#  MarketData
#client = Market(url='https://api.kucoin.com')
# 

import asyncio
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient

async def main():
    async def deal_msg(msg):
        if msg['topic'] == '/spotMarket/level2Depth5:BTC-USDT':
            print(msg["data"])
        elif msg['topic'] == '/spotMarket/level2Depth5:KCS-USDT':
            print(f'Get KCS level3:{msg["data"]}')

    # is public
    client = WsToken()
    #is private
    # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
    # is sandbox
    #client = WsToken(is_sandbox=True)
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
    # await ws_client.subscribe('/market/ticker:BTC-USDT,ETH-USDT')
    await ws_client.subscribe('/spotMarket/level2Depth5:BTC-USDT,KCS-USDT')
    while True:
        await asyncio.sleep(60, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())












'''

# or connect to Sandbox
client = Market(url='https://openapi-sandbox.kucoin.com')
client = Market(is_sandbox=True)

# get symbol kline
#klines = client.get_kline('BTC-USDT','1min')

# get symbol ticker
#server_time = client.get_server_timestamp()

api_key = '61de46c92b968a000152e31f'
api_secret = '32bfd80e-a7e0-4cf2-8029-24c135599984'
api_passphrase = 'SepactMfdst'

tickers = client.get_ticker('KCS-USDT')
print(tickers)

# Trade
from kucoin.client import Trade
client = Trade(key='', secret='', passphrase='', is_sandbox=False, url='')

# or connect to Sandbox
# client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

# place a limit buy order
order_id = client.create_limit_order('BTC-USDT', 'buy', '1', '8000')

# place a market buy order   Use cautiously
order_id = client.create_market_order('BTC-USDT', 'buy', size='1')

# cancel limit order
client.cancel_order('5bd6e9286d99522a52e458de')

# User
from kucoin.client import User
client = User(api_key, api_secret, api_passphrase)

# or connect to Sandbox
# client = User(api_key, api_secret, api_passphrase, is_sandbox=True)

address = client.get_withdrawal_quota('KCS')
'''






















