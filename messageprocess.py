


def processMessage(message):
	tradeObj = {}
	#check for message relevace
	substrings = ['TP1','TP2','TP3','TP4']
	tpArr = []
	crypy = ""
	splitMessage= message.splitlines()
	for element in splitMessage:
		if "/" in element:
			strArr = element.partition('/')
			crypy =strArr[0]
			print(f'trading pair is {crypy}.')
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
	print(tradeObj)



if __name__ == '__main__':
	messages1 = "ETH/USD\nTP1: 4150\nTP2: 4250\nTP3: 4400\nSL: 3988"
processMessage(messages1)