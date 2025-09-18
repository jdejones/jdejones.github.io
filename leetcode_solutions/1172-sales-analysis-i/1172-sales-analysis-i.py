import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('seller_id')['price'].sum().reset_index()
    df = df.loc[df.price == df.price.max()]
    return df.seller_id.to_frame()
