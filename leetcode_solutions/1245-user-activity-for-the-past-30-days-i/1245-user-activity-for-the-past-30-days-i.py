import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    end_date = pd.to_datetime('2019-07-27')
    tdelta = pd.Timedelta(days=30)
    df = (
        activity
        .loc[(activity.activity_date.between(end_date-tdelta, end_date, inclusive='right'))]
    )
    
    group = df.groupby('activity_date')['user_id'].nunique().reset_index()
    group = group.rename(columns={'activity_date': 'day', 'user_id': 'active_users'})

    return group
