import csv

# open the file in universal line ending mode 
with open('TWS_vwap_order.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# extract the variables you want
contracts = data['contract']
exchanges = data['exchange']
trade_types = data['trade_type']
quantitys = data['quantity']
order_types = data['order_type']
max_perc_advs = data['max_percentage_ADV']
start_times = data['start_time']
end_times = data['end_time']
allow_trad_past_ends = data['allow_trading_past_end_time']
attempt_liquids = data['attempt_to_never_take_liquidity']

print contracts, "\n", exchanges, max_perc_advs