
#%% Create database buoy_data with header values from all_columns
import sqlite3

all_columns = ['YY','MM','DD','hh', 'mn', 'WDIR', 'WSPD', 'GST', 'WVHT','DPD','APD', 'MWD', 'PRES','ATMP', 'WTMP', 'DEWP', 'VIS','TIDE']

conn = sqlite3.connect('buoy_data.db')
cur = conn.cursor()
columns_sql = ', '.join([f'"{col}" NUMERIC' for col in all_columns])
cur.execute(f"CREATE TABLE IF NOT EXISTS buoy_data ({columns_sql});")

# %% Add 2001 to 2024 data to buoy_data
for year in range(2001, 2025):
    filename = f'data/{year}.txt'
    
    with open(filename) as f:
        headers = None
        for line in f:
            if not headers: headers = line.strip().strip('#').split()
                
            # Skip non-data lines
            if line.startswith('#') or line.startswith('Y'):
                continue

            values = line.strip().split()

            # Add minute value of 0 for data with no minute (pre-2005)
            if len(values) != len(all_columns):
                values.insert(4,'0')

            # Add tide values 
            
            assert(len(values) == len(all_columns))

            cur.execute(f'INSERT INTO buoy_data VALUES ({",".join(["?"]*len(all_columns))})', values)
    
    conn.commit()

conn.close()

