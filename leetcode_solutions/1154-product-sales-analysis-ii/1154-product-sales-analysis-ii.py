import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('product_id')['quantity'].sum().reset_index()
    df['total_quantity'] = df.quantity
    df = df.drop('quantity', axis=1)
    return df
