from ib.opt import Connection, message
from ib.ext.Contract import Contract
from ib.ext.Order import Order
import sys
from time import sleep
#imports all the libraries from IBpy
#you can also import the libraries from IB API, its something like "from ibapi" 

def make_contract(symbol, sec_type, exch, prim_exch, curr):
#this function creates your contract, there are many more parameters you can add in
    Contract.m_symbol = symbol #ticker
    Contract.m_secType = sec_type #security type
    Contract.m_exchange = exch  
    Contract.m_primaryExch = prim_exch 
    Contract.m_currency = curr
    return Contract

def check_order(Order):
    #dont worry about this, Im trying to test something out
	return Order.m_lmtPrice
	print Order.m_lmtPrice
	print('hi')

def make_order(action,quantity, price = None):
# this is where you place the order to the API

    if price is not None: #you specify the price
        order = Order()
        order.m_orderType = 'LMT'
        order.m_totalQuantity = quantity
        order.m_action = action
        order.m_lmtPrice = price
         
    else: #you put "None" as price, you get market order
        order = Order()
        order.m_orderType = 'MKT'
        order.m_totalQuantity = quantity
        order.m_action = action

        
    return order

#this parts opens up the tracker file, reads it for the counter variable 
oidfile = open('oid_tracker.txt', 'r') 
cid = oidfile.readline()
oidfile.close()
print(cid)
oid = int(cid)

#these are just hard coded for now, but the arrays of information needed
stocks = ['FB','AAPL', 'GOOG']
prices = [137.59, None,150.98]
amounts = [2,5,10] #these amounts are multiplied by 100
transacs = ['BUY', 'SELL', 'BUY']

#creates connection, the important info are the ports and client ID
conn = Connection.create(port=7496, clientId=999)
conn.connect()

#loops through the arrays so that each order can be filled 
for stock,price,amount,transac in zip(stocks,prices,amounts,transacs):
	                
	cont = make_contract(stock, 'STK', 'SMART', 'SMART', 'USD')	#hardcoded stuff but can be dynamic
	offer = make_order(transac, amount, price) 
	conn.placeOrder(oid, cont, offer) #places the order
	check = check_order(offer) #this line is for me, its not useful
	oid += 1 
	print(stock + "\n") #again some debugging mechanisms
	print(oid)


conn.disconnect() #good practice to disconnect after you place the orders

#need to update the counter for next time.
replaceoid = open('oid_tracker.txt', 'w')
replaceoid.write("%d" % oid)
replaceoid.close()


    

