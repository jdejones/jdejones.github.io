import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer['name'].loc[(customer['referee_id'] != 2) | (customer['referee_id'].isna())].to_frame()