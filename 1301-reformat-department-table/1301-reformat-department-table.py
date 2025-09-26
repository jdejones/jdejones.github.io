import pandas as pd
import calendar

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    month_abbr = list(calendar.month_abbr[1:])

    department['month'] = pd.Categorical(department['month'], categories=month_abbr)

    df = department.pivot(columns='month', values='revenue', index='id')
    for month in month_abbr:
        if month not in df.columns:
            df[month] = None
        

    cols = [_ + '_Revenue' for _ in df.columns if _ != 'id']
    cols = ['id'] + cols
    df = df.reset_index()
    df.columns = cols

    return df