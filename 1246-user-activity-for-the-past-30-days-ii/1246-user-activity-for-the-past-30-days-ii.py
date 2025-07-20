import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    end_date = pd.to_datetime('2019-07-27', format='%Y-%m-%d')
    start_date = end_date - pd.Timedelta(days=29)
    df = activity.loc[activity.activity_date.between(start_date, end_date)]
    df = df.groupby('user_id')['session_id'].nunique().reset_index()
    if len(df) == 0:
        output = pd.Series([0], name='average_sessions_per_user')
        return output.to_frame()
    output = pd.Series([round(sum(df['session_id']) / len(df), 2)], name='average_sessions_per_user')
    return output.to_frame()