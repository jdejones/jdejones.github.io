import pandas as pd

def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:
    employees['rank'] = employees.groupby('dept')['salary'].rank(method='dense', ascending=False)
    df = employees[['emp_id', 'dept']].loc[employees['rank']==2].sort_values('emp_id')
    return df