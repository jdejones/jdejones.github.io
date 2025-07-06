# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment['year_month'] = pd.to_datetime(amazon_shipment['shipment_date'].dt.strftime('%Y-%m'))
amazon_shipment['id'] = amazon_shipment['shipment_id'].astype(str) + '_' + amazon_shipment['sub_id'].astype(str)
df = amazon_shipment.groupby('year_month')['id'].nunique().to_frame('count').reset_index()
return df
