import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[['name', 'weight']].loc[animals.weight > 100].sort_values('weight', ascending=False)['name'].to_frame()
