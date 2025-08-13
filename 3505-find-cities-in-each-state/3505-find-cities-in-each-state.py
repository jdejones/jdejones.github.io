import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    df = cities.sort_values('city')
    df = df.groupby('state')['city'].agg(', '.join).reset_index()
    df.columns = ['state', 'cities']
    return df