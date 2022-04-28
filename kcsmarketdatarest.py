from kucoin.client import Market

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