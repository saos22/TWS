from ib.opt import Connection, message
from ib.ext.Contract import Contract
from ib.ext.Order import Order
import sys
from time import sleep

def make_contract(symbol, sec_type, exch, prim_exch, curr):

    Contract.m_symbol = symbol
    Contract.m_secType = sec_type
    Contract.m_exchange = exch
    Contract.m_primaryExch = prim_exch
    Contract.m_currency = curr
    return Contract

def check_order(Order):
	return Order.m_lmtPrice
	print Order.m_lmtPrice
	print('hi')

def make_order(action,quantity, price = None):

    if price is not None:
        order = Order()
        order.m_orderType = 'LMT'
        order.m_totalQuantity = quantity
        order.m_action = action
        order.m_lmtPrice = price
         
    else:
        order = Order()
        order.m_orderType = 'MKT'
        order.m_totalQuantity = quantity
        order.m_action = action

        
    return order
oidfile = open('oid_tracker.txt', 'r') 
cid = oidfile.readline()
oidfile.close()
print(cid)

oid = int(cid)
stocks = ['FB']
prices = [137.59, 120.34,150.98]
amounts = [2,5,10]
# while __name__ == "__main__":

conn = Connection.create(port=7496, clientId=999)
conn.connect()

for stock,price,amount in zip(stocks,prices,amounts):
	                
	cont = make_contract(stock, 'STK', 'SMART', 'SMART', 'USD')	
	offer = make_order('BUY', amount, price)
	conn.placeOrder(oid, cont, offer)
	check = check_order(offer)
	oid += 1
	print(stock + "\n")
	print(oid)


conn.disconnect()


replaceoid = open('oid_tracker.txt', 'w')
replaceoid.write("%d" % oid)

replaceoid.close()

    #x = raw_input('enter to resend')
    

