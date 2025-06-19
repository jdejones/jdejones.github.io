import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee.employee_id.value_counts()
    count1 = counts[counts == 1].index
    df = employee[['employee_id', 'department_id']].loc[
        (employee.primary_flag == 'Y') |
        (employee.employee_id.isin(count1))
    ]
    return df
