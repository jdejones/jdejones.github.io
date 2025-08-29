import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.customer_number.value_counts().reset_index().loc[:0, 'customer_number'].to_frame()
