import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged_df = product.merge(sales)
    s8 = merged_df.loc[merged_df.product_name == 'S8']
    iphone = merged_df.loc[merged_df.product_name == 'iPhone']
    df = (merged_df.loc[(merged_df.buyer_id.isin(s8.buyer_id.to_list())) & 
         (~merged_df.buyer_id.isin(iphone.buyer_id.to_list()))]
         )
    return df.buyer_id.drop_duplicates().to_frame()
