# Trade
from kucoin.client import Trade
#from kucoin.client import Market
#client = Trade(key='61de46c92b968a000152e31f', secret='32bfd80e-a7e0-4cf2-8029-24c135599984', passphrase='SepactMfdst', is_sandbox=True, url='https://openapi-sandbox.kucoin.com')
from pycoingecko import CoinGeckoAPI




'''
def testFileConncetion(msgInput):

	print(msgInput)
	tradePair = msgInput['Curr'] + '-USDT'
	print(tradePair)
	action = 'buy'
	quantity =
	#client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)
	order_id = client.create_limit_order('KCS-USDT', 'buy', '1', '21.60')

	#OrderConfirmation = client.get_recent_orders()
	print('Order Confirmed')

def tradeCallToKCS(msgInput):


	# or connect to Sandbox
	api_key = '61de46c92b968a000152e31f'
	api_secret = '32bfd80e-a7e0-4cf2-8029-24c135599984'
	api_passphrase = 'SepactMfdst'
	client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)
	order_id = client.create_limit_order('KCS-USDT', 'buy', '1', '21.60')

	print('Order Confirmed')
'''
#################################
#################################
##check and grab current prices
################################
def getPrices(cgObj,curr):
	try:
		return cg.get_price(ids=curr, vs_currencies='usd')
	except:
		print('error no such currency')




#########################################
#########################################
##def getTradeParams() Either from telegram or manual entry, sl, tp etc
##########################################


#################################
#################################
## def spotBuyCall()
################################

def tradeCallToKCS(msgInput):

	#tradePair = msgInput['Curr'] + '-USDT'
	# or connect to Sandbox
	api_key = '630faf0e2b968a000153d6d9'
	api_secret = 'ef6a993d-e3bb-4b6a-a4c4-c33c130bb80b'
	api_passphrase = 'SepactMfdst1114'
	client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)
	# get currencies
	currencies = client.get_currencies()
	#order_id = client.create_limit_order('KCS-USDT', 'buy', '1', '21.60')
	print(currencies)
	print('Order Confirmed')
#################################
#################################
## def spotSellCall()
################################
if __name__ == '__main__':

	#cg = CoinGeckoAPI()
	#print(cg.get_price(ids='bitcoin', vs_currencies='usd'))
