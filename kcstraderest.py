# Trade
from kucoin.client import Trade
#from kucoin.client import Market
#client = Trade(key='61de46c92b968a000152e31f', secret='32bfd80e-a7e0-4cf2-8029-24c135599984', passphrase='SepactMfdst', is_sandbox=True, url='https://openapi-sandbox.kucoin.com')

# or connect to Sandbox
api_key = '61de46c92b968a000152e31f'
api_secret = '32bfd80e-a7e0-4cf2-8029-24c135599984'
api_passphrase = 'SepactMfdst'
client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True) 
#priceClient = Market(url='https://openapi-sandbox.kucoin.com')
#priceClient = Market(is_sandbox=True)
#AssetTicker = priceClient.get_ticker('KCS-USDT')
#print(AssetTicker)
# place a limit buy order
order_id = client.create_limit_order('KCS-USDT', 'buy', '1', '21.60')

#OrderConfirmation = client.get_recent_orders()
print('Order Confirmed')

# place a market buy order   Use cautiously
#
# cancel limit order
#client.cancel_order('5bd6e9286d99522a52e458de')