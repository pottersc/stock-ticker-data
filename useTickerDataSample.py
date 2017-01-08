import stockTickerData
import datetime

"""
Example usage of ticker data that extracts minute ticker data for 'SPY' for
a single day and then prints the entire pandas dataframe result to the console
"""
stockTickerData = stockTickerData.StockTickerData('mongodb://localhost:27017/')
date_start = datetime.date(2017, 1, 6)
date_end = datetime.date(2017, 1, 6)
minute_quotes_df = stockTickerData.get_quotes('SPY', 60, date_start=date_start, date_end=date_end)
print(minute_quotes_df)

