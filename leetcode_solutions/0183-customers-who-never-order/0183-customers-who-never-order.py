import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers['name'].loc[~customers['id'].isin(orders['customerId'])]
    df.name = 'Customers'
    return df.to_frame()
