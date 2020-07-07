from Robinhood import Robinhood

robinhood_client = Robinhood()
robinhood_client.login(username='yourusername@mail.com', password='yourpassword')

# Enter your 6 digits Robinhood code in your phone.

qr_code = '1234567890qwerty'
robinhood_client = Robinhood()
robinhood_client.login(username='yourusername@mail.com', password='yourpassword', qr_code=qr_code)

# Account Management:

# summary of your current portfolios
robinhood_client.portfolios()
# Current positions and history positions
robinhood_client.positions()

# Accessing Market Data:

# Get stock information, url needed to make buy/sell order.
# Note: Sometimes more than one instrument may be returned for a given stock symbol
stock_instrument = robinhood_client.instruments('MSFT')[0]

# Get a stock's quote
stock_quote = robinhood_client.quote_data('MSFT')

# Market price
print(stock_quote['last_trade_price'])

# If you want history price data:

# one week of 5minut OHLC info, you can change '5minute' to '10minute'|'30minute'
robinhood_client.get_historical_quotes('MSFT', '5minute', 'week')

# one week of daily OHLC info,
robinhood_client.get_historical_quotes('MSFT', 'day', 'week')

# one year of daily OHLC info,
robinhood_client.get_historical_quotes('MSFT', 'day', 'year')

# Currently, API only supports interval as 5minute | 10minute | 30minute | day | week. 
# And date range as day | week | year | 5year | all.

# Trading from API:

# For ticker DWT
stock_instrument=robinhood_client.instruments('DWT')[0]
buy_order=robinhood_client.place_market_buy_order(stock_instrument['url'], 'DWT', 'GFD', 1)
sell_order=robinhood_client.place_market_sell_order(stock_instrument['url'], 'DWT', 'GFD', 1)
# Here GFD means good for the day, which will be canceled if not filled today. 
# Also, you can set GTC which means good until cancel.

# All supported order function:
# place_market_buy_order
# place_market_sell_order
# place_limit_buy_order
# place_limit_sell_order
# place_stop_loss_sell_order
# place_stop_limit_sell_order

