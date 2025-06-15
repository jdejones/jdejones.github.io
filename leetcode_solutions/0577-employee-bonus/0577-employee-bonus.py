import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(bonus, how='outer', on='empId')
    return df[['name', 'bonus']].loc[(df.bonus < 1000) | (df.bonus.isna())]
