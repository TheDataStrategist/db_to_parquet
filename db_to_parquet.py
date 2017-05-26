#!/usr/bin/env python3
"""The module desciption goes here

Usage:

  python3 moduleName.py <arg1>
"""

import sys
import sqlite3
import pandas as pd
import fastparquet as fp

sqlite_file = 'event.sqlite3'
table_name='event'

def main(param):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    event_df=pd.read_sql('SELECT * FROM event',conn)
    print('1):', event_df.head(5))
    fp.write(table_name+'.parq', event_df, compression='GZIP')

if __name__ == '__main__':
    main(sys.argv)
