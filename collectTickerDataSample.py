import stockTickerData

"""
Example of Storing historical stock ticker data for a set of stocks as identified
in file 'ticker_symbols.txt' into a local mongo database for later retrieval.
In this example the previous 5 days worth of minute data are stored
This routine is best run as a daily scheduled task to collect historical data
over an extended period of time.
"""
stockTickerData = stockTickerData.StockTickerData('mongodb://localhost:27017/')
stockTickerData.load_ticker_data_to_db_from_list("ticker_symbols.txt", 60, 5)

