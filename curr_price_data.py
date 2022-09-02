#  MarketData
from kucoin_futures.client import Market
import time
client = Market(url='https://api-futures.kucoin.com')
# client = Market()
# or connect to Sandbox
# get symbol ticker
def getPriceData(curr):
    #curr_pair = curr+'USDTM'
    price_data = client.get_ticker(curr)
    return price_data

def get_contract_detail(curr):
    contract_detail = client.get_contract_detail(curr)
    return contract_detail

if __name__ == '__main__':
    #print(client.get_contract_detail('ETHUSDTM'))
    print(getPriceData('ADAUSDTM'))
    #time.sleep(5)
