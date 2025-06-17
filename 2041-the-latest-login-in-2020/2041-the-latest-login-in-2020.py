import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    df = logins
    df = df.loc[(df.time_stamp > '2020-01-01 00:00:00') & 
                  (df.time_stamp < '2020-12-31 23:59:59')]
    df.rename(columns={'time_stamp': 'last_stamp'}, inplace=True)
    return df.groupby('user_id')[['user_id', 'last_stamp']].max()