import configparser
import json
import re
import time
import string as str
from kucoin_futures.client import Trade
from kucoin.client import Client
from kucoin_futures.client import Trade
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from kucoin_futures.client import Market
import curr_price_data
import messageprocess
import asyncio
from telethon.tl.types import (
PeerChannel
)

from telethon import TelegramClient
'''
api_id = 12223282
api_hash = 'dd27c92671e9b82b788c8b7d93716032'

client = TelegramClient('anon3', api_id, api_hash)
user_input_channel = 'https://t.me/autotrigger'
async def sendMessage(message):
    # Now you can use all client methods listed below, like for example...
    await client.send_message(user_input_channel, message)

with client:
    client.loop.run_until_complete(sendMessage('bye'))

'''










async def sendMessage(message):
    # Now you can use all client methods listed below, like for example...
    await client.send_message(user_input_channel, message)

api_id = 12223282
api_hash = 'dd27c92671e9b82b788c8b7d93716032'


client = TelegramClient('anon3', api_id, api_hash)

# Here you define the target channel that you want to listen to:
user_input_channel = 'https://t.me/autotrigger'
'''
def processMessage(message):
	tradeObj = {}
	#check for message relevace
	substrings = ['TP1','TP2','TP3','TP4']
	tpArr = []
	crypy = ""
	splitMessage= message.splitlines()
	entryFlag = False
	for element in splitMessage:

		if entryFlag:
			entryString = element.partition('-')
			range_entry = [entryString[0],entryString[2]]
			entryFlag = False
		#print(element)
		if "/" in element:
			strArr = element.partition('/')
			crypy =strArr[0]
			#print(f'trading pair is {crypy}.')
		if "Entry" in element:
			entryFlag = True

		if "TP" in element:
			tpString  = element.partition(':')
			tpPrice = tpString[2]
			tpArr.append(tpPrice.strip())
		if "SL" in element:
			slString = element.partition(':')
			sl = slString[2].strip()

	tradeObj['Curr'] = crypy
	tradeObj['TP'] = tpArr
	tradeObj['SL'] = sl

	long_short = ''
	tp_diff = float(tpArr[0].replace(',','')) - float(tpArr[1].replace(',',''))
	print(tp_diff)
	if tp_diff < 0:
		long_short = 'buy'
	else:
		long_short = 'sell'

	tradeObj['entry'] = range_entry
	tradeObj['side'] = long_short
	print(tradeObj)
	return tradeObj
'''
def tradeCallToKCS(tradeObj):
	market_client = Market(url='https://api-futures.kucoin.com')
	# client = Market()
	# or connect to Sandbox
	trade_pair = tradeObj['Curr'].strip() + 'USDTM'
	trade_side = tradeObj['side']
	trade_leverage = 1
	trade_size = 10
	entryArr = tradeObj['entry']
	entry_to_float1 = float(entryArr[0].replace(',',''))
	entry_to_float2 = float(entryArr[1].replace(',',''))

	price_data = curr_price_data.getPriceData(trade_pair)
	price = float(price_data['price'])
	contract_detail = curr_price_data.get_contract_detail(trade_pair)
	multiplier = contract_detail['multiplier']


	print(trade_pair)
	print(entry_to_float1)
	print(entry_to_float2)


	api_key = '630fe5b137a609000198dad4'
	api_secret = '10ec6fd4-1dcd-447b-b0cf-521aab359bd7'
	api_passphrase = 'SepactMfdst1114'
	# Trade
	client_trade = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=True, url='https://api-sandbox-futures.kucoin.com')

	order_id = ''
	# or connect to Sandbox
	# client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)
	while True:
		print(f'price: {price}, entryLower: {entry_to_float2}, entryUpper: {entry_to_float1}' )
		if(trade_side == 'buy'):
			if(price >= entry_to_float2 and price<= entry_to_float1):
				cost_of_one_lot = multiplier * price
				print(multiplier)
				print(cost_of_one_lot)
				dollar_per_trade = 20
				lot_quantity = int(dollar_per_trade/cost_of_one_lot)
				print(lot_quantity)
				order_id = client_trade.create_limit_order(trade_pair, trade_side, trade_leverage, lot_quantity, price)
				print(order_id)

				print('Order Confirmed')

				#client.loop.run_until_complete(sendMessage('Trade_executed'))

				#client.send_message(user_input_channel, "Trade executed")
				break

		if(trade_side == 'sell'):
			if(price <= entry_to_float2 and price>= entry_to_float1):

				order_id = client_trade.create_limit_order(trade_pair, trade_side, trade_leverage, '2', price)
				print(order_id)

				print('Order Confirmed')
				client.send_message(user_input_channel, "Trade executed")
				break

		time.sleep(5)
		priceArr = curr_price_data.getPriceData(trade_pair)
		price = float(priceArr['price'])


	return order_id

#if __name__ == '__main__':

	#tradeCallToKCS()

@client.on(events.NewMessage(chats=user_input_channel))
async def NewMessageListener(event):
	message = event.message.message
	tradeObj = messageprocess.processMessage(message)
	opened_position = tradeCallToKCS(tradeObj)




with client:
	client.run_until_disconnected()
