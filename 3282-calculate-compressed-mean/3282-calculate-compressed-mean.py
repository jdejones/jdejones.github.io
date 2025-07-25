import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    orders['temp'] = orders['item_count'] * orders['order_occurrences']
    return pd.DataFrame({'average_items_per_order':
                        [round(orders['temp'].sum() / orders['order_occurrences'].sum(), 2)]})