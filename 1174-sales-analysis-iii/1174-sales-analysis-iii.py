import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    is_btwn = sales.loc[sales.sale_date.between('2019-01-01', '2019-03-31', inclusive='both')].product_id.to_list()
    not_btwn = sales.loc[~sales.sale_date.between('2019-01-01', '2019-03-31', inclusive='both')].product_id.to_list()
    
    merged_df = product.merge(sales, how='outer')

    return (merged_df[['product_id', 'product_name']]
            .loc[
                (merged_df.product_id.isin(is_btwn)) & 
                (~merged_df.product_id.isin(not_btwn))
                ]
            .drop_duplicates()
            )