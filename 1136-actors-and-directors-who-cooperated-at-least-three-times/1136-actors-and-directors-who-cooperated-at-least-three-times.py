import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index()
    return df[['actor_id', 'director_id']].loc[df[0] >= 3]