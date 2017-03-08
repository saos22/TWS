from ib.opt import Connection, message
from ib.ext.Contract import Contract
from ib.ext.Order import Order
import sys
def make_contract(symbol, sec_type, exch, prim_exch, curr):

    Contract.m_symbol = symbol
    Contract.m_secType = sec_type
    Contract.m_exchange = exch
    Contract.m_primaryExch = prim_exch
    Contract.m_currency = curr
    return Contract



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


cid = 10105
stocks = ['MSFT', 'AAPL']

#while __name__ == "__main__":

conn = Connection.create(port=7496, clientId=999)
conn.connect()

for stock in stocks:
	oid = cid
	cont = make_contract(stock, 'STK', 'SMART', 'SMART', 'USD')
    	
	offer = make_order('BUY', 1, 200)
	conn.placeOrder(oid, cont, offer)
	cid += 1

conn.disconnect()
    #x = raw_input('enter to resend')
    

