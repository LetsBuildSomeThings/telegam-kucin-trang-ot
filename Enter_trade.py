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

api_key = '630fe5b137a609000198dad4'
api_secret = '10ec6fd4-1dcd-447b-b0cf-521aab359bd7'
api_passphrase = 'SepactMfdst1114'
    # Trade
client_trade = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase,
is_sandbox=True, url='https://api-sandbox-futures.kucoin.com')

def demoTradeCalls():

    params = {'stop': 'loss', 'stopPrice': 1500 , 'stopPriceType': 'TP'}
    order_id = client_trade.create_limit_order('XBTUSDTM', 'buy', 1, 1, 2000.0,params=params)
    #add stop order
    print(order_id)

def cancelLimitOrders(curr):
    client_trade.cancel_all_limit_order(curr)




def tradeCallToKCS(tradeObj):
    #URL -  change for Sanbox/Real
    market_client = Market(url='https://api-futures.kucoin.com')
    trade_pair = tradeObj['Curr'].strip() + 'USDTM'
    trade_side = tradeObj['side']
    trade_leverage = 1
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

    '''
    Got all contract details begin trading and while true loop until entry trade done
    '''
    api_key = '630fe5b137a609000198dad4'
    api_secret = '10ec6fd4-1dcd-447b-b0cf-521aab359bd7'
    api_passphrase = 'SepactMfdst1114'
    # Trade
    client_trade = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase,
    is_sandbox=True, url='https://api-sandbox-futures.kucoin.com')
    order_id = ''
    # or connect to Sandbox
    # client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)
    print(f'price: {price}, entryLower: {entry_to_float2}, entryUpper: {entry_to_float1}' )
    if(trade_side == 'buy'):
        cost_of_one_lot = multiplier * price
        print(multiplier)
        print(cost_of_one_lot)
        dollar_per_trade = 20
        lot_quantity = int(dollar_per_trade/cost_of_one_lot)
        print(lot_quantity)
        if(price >= entry_to_float2 and price<= entry_to_float1):

            order_id = client_trade.create_limit_order(trade_pair, trade_side, trade_leverage, lot_quantity, price)
            #add stop order
            print(order_id)
            print('Order Confirmed')

        if(price<=entry_to_float2):
            order_id = client_trade.create_limit_order(trade_pair, trade_side, trade_leverage, lot_quantity, price)
            #add stop order
            print(order_id)
            print('Order Confirmed')

        else:
            order_id = client_trade.create_limit_order(trade_pair, trade_side, trade_leverage, lot_quantity, entry_to_float1)
            #add stop order
            print(order_id)
            print('Order Confirmed')



            if(trade_side == 'sell'):
                if(price <= entry_to_float2 and price>= entry_to_float1):

                    order_id = client_trade.create_limit_order(trade_pair, trade_side, trade_leverage, '2', price)
                    print(order_id)

                    print('Order Confirmed')
                    #client.send_message(user_input_channel, "Trade executed")


                    #time.sleep(5)
                    #priceArr = curr_price_data.getPriceData(trade_pair)
                    #price = float(priceArr['price'])
            return order_id

if __name__ == '__main__':
    #demoTradeCalls();
    #client_trade.cancel_order('63128de241a533000104a462')
    #print(client_trade.get_position_details('ADAUSDTM'))
    params = {'stop': 'down', 'stopPrice': 0.22 , 'stopPriceType': 'TP'}
    client_trade.create_limit_order(symbol='ADAUSDTM',side='buy', lever=1, size=2, price=0.32, params=params)
    #print(client_trade.get_order_list())
