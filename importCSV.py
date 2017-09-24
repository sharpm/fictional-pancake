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
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame()
    #if 'SPY' not in symbols:  # add SPY for reference, if absent
     #   symbols.insert(0, 'SPY')

     #dateparse = lambda x: [pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for d in dates]

    df_temp = pd.read_csv(symbol_to_path(logfile),
                             parse_dates=True, usecols=['time', 'type', 'pair', 'vol', 'price', 'cost', 'fee'])
        #df_temp = df_temp.rename(Columns={'time': 'Date'})
    #somelist = df_temp['time'].tolist()
    datelist = df_temp['time'].tolist() 
    timeformat = pd.to_datetime(pd.Series(datelist))
    #print df_temp
    df = df.join(df_temp)
    print timeformat
    return df


def sort_date():
    # Define a date range
    dates = pd.date_range('03/25/2017 04:18:32.3478', '03/25/2017 06:04:17.4039')

    # Choose stock symbols to read
    krakenlog = 'trades'
    
    # Version Stamp
    print ('Pandas Version:'), pd.__version__
    # Get stock data
    df = get_data(krakenlog, dates)
    print df


if __name__ == "__main__":
    sort_date()


