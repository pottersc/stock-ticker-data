# stock-ticker-data
The stock-ticker-data application was developed to provide a free source of historical minute based ticker data
There are plenty of paid services that allow people to access minute ticker data, but the only free sources that
I could find only go back 15 days of historical data.  The stock-ticker-data application addresses this issue by 
making daily calls to the free ticker data services and storing the data in a local database for future access. 
The tikcer data maintained includes open, high, low, close, volume, and datestamp in minute intervals.
The application is written in Python, uses a Mongo database for storage, and returns historical minute stock ticker
data in a pandas dataframe.

### Usage
See 'collectTickerDataSample.py' for usage example on collecting tikcer data
See 'useTickerDataSample.py' for usage example on retrieving ticker data

### Development and DB setup
python -m pip install pymongo

install mongdo db as outlined in https://docs.mongodb.com/manual/installation/

create mongo config file then install mongodb service (example below)
"C:\Program Files\MongoDB\Server\3.2\bin\mongod.exe" --config "E:\Data\mongo_data\mongod.cfg" --install

to start service: 'net start MongoDB'
to stop service: 'net stop MongoDB'

