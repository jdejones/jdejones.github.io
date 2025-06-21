import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    _paid = user_activity.user_id.loc[user_activity['activity_type'] == 'paid'].to_list()
    _df = user_activity.loc[(user_activity['user_id'].isin(_paid)) &
                            ((user_activity['activity_type'] == 'free_trial') | 
                            (user_activity['activity_type'] == 'paid'))]
    type_free = _df[['user_id', 'activity_duration']].loc[_df['activity_type'] == 'free_trial']
    type_free.columns = ['user_id', 'trial_avg_duration']
    type_paid = _df[['user_id', 'activity_duration']].loc[_df['activity_type'] == 'paid']
    type_paid.columns = ['user_id', 'paid_avg_duration']
    df = pd.merge(type_free, type_paid, on='user_id')
    df = (df.groupby(['user_id'], as_index=False)[[
        'trial_avg_duration', 'paid_avg_duration'
        ]]
        .mean()
    )
    df['trial_avg_duration'] = (df['trial_avg_duration'] + 1e-8).round(2)
    df['paid_avg_duration'] = (df['paid_avg_duration'] + 1e-8).round(2)
    return df