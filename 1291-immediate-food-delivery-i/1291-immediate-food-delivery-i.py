import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['type'] = 'scheduled'
    delivery['type'].loc[delivery.order_date == delivery.customer_pref_delivery_date] = 'immediate'

    if 'immediate' in delivery.type.to_list():
        isimmediate = delivery['type'].value_counts(normalize=True)['immediate']

        return (
            pd.DataFrame({'immediate_percentage': [round(isimmediate * 100, 2)]})
        )
    
    return (
        pd.DataFrame({'immediate_percentage': [0.0]})
    )