# Import your libraries
import pandas as pd
"""
This problem would have been clearer with better defined columns.
Each customer in customers has a unique id.
Each order in orders has a unique id.
Primary keys:
    customerss -> id
    orders -> cust_id
Each cust_id in orders can be found in multiple rows.
So, id from customers and cust_id from orders must be used to merge the 2 dataframes.
"""
# Start writing code
df = customers[['id', 'first_name', 'last_name', 'city']].merge(orders[['cust_id', 'order_details']], how='left', left_on='id', right_on='cust_id')
return df[['first_name', 'last_name', 'city', 'order_details']].sort_values(['first_name', 'order_details'])
