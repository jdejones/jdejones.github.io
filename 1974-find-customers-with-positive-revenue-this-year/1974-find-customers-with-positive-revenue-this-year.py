import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    df = (customers.customer_id.loc[(customers.year == 2021) &
                                    (customers.revenue > 0)])
    return df.to_frame()