import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    df = point.sort_values('x')
    df['diff'] = df['x'].diff().abs()
    return pd.DataFrame({'shortest': [df['diff'].min()]})