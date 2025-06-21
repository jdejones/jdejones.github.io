import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(employee, how='left', left_on='id', right_on='managerId')
    df = employee.name_y.loc[employee.salary_y > employee.salary_x].to_frame()
    df.columns = ['Employee']
    return df