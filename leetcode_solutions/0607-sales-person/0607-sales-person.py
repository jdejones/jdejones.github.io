import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    company = company.rename(columns={'name': 'company_name'})
    df = company.merge(orders, how='outer', on='com_id')
    red_ids = df.loc[df.company_name == 'RED'].sales_id
    return sales_person.loc[~sales_person.sales_id.isin(red_ids.to_list())].name.to_frame()
