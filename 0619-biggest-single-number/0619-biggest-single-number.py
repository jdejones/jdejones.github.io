import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    uniques = my_numbers.num.value_counts().loc[my_numbers.num.value_counts() == 1].index
    if len(uniques) > 0:
        val = max(uniques)
        return pd.DataFrame({'num': [val]})
    return pd.DataFrame({'num': [None]})