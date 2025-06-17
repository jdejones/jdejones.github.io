import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time'] = employees['out_time'] - employees['in_time']
    gb =  employees.groupby(['event_day', 'emp_id'])['time'].sum().to_frame()
    df = pd.DataFrame({gb.index.names[0]: [item[0] for item in gb.index], gb.index.names[1]: [item[1] for item in gb.index], 'time': gb['time'].values})
    #df =  employees.groupby(['event_day', 'emp_id'])['time'].sum().to_frame()
    df.rename(columns={'event_day': 'day', 'time': 'total_time'}, inplace=True)
    return df
    #df['day'] = pd.to_datetime(df['day'])
    #return df.sort_values('day')