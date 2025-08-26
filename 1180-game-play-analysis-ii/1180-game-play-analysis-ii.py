import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    group = activity.groupby('player_id')['event_date'].min().reset_index()
    df = activity.merge(group, on=['player_id', 'event_date'])
    return df[['player_id', 'device_id']]