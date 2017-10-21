"""Trade Import Utility"""

"""
- Define each month date ranges
- Import date and trade data
- Calculate open and close positions
- Write to new CSV file
"""

import os
import datetime as dt
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(logfile, dates):
    """Read trade data (adjusted close) for given symbols from CSV files."""
    
    #dateparse = lambda x: [pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for d in dates] # Create custom time format

    df_temp = pd.read_csv(symbol_to_path(logfile),
        parse_dates=True, usecols=['time', 'type', 'pair', 'vol', 'price', 'cost', 'fee'])
    
    df_temp['time'] = pd.to_datetime(df_temp['time'])   # Change date string to Timestamp and drop time component
    
    #df_temp = df_temp.rename(columns={"time": "Date"}) #Rename column
    #df=pd.DataFrame(index=dates) # Create dataframe with Timestamp index
    
    df=df_temp
        
    return df
    
def record_trade(df):
    trade_log = df.copy
    BTC_pair = "XBTCZUSD"
    ETH_pair = "XETHZUSD"
    BTC_count = 0
    ETH_count = 0
    
    #print df['pair'].item
    
    # Filter dataframe by currency pair
    p_group = df.groupby('pair') 
    new_group = p_group.get_group(ETH_pair)
    print new_group
    
    for i in new_group.index:
        if  new_group.loc[i].type == "buy":
            ETH_count = ETH_count + new_group.loc[i].vol
            while ETH_count
         #   p_group.get_group(ETH_pair).vol[i].values
         #   print p_group.get_group(ETH_pair).vol[i:].values
         #   print p_group.get_group(ETH_pair).type[0]
        
        
        
        #if df.type[i:].values = "buy":
         #   ETH_count = ETH_count + df.vol[i:].values
        #print df.type
        #while ETH_count != 0:
        
   

def sort_date():
    # Define a date range. Currently unused.
    dates = pd.date_range('2017-03-25', '2017-03-26')

    # Choose trading log to read
    krakenlog = 'trades'
    
    # Get trade data
    df = get_data(krakenlog, dates)
    
    # Select rows based on month
    t_df = df[df.time.dt.month == 03] 
    
    # Separate raw trade data into actual trades
    record_trade(t_df)
     

if __name__ == "__main__":
    # Version Stamp
    print ('Pandas Version:'), pd.__version__
    sort_date()
