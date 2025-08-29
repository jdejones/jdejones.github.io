import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    #Find distinct salaries
    df = pd.Series(employee.salary.unique(), name='salary').sort_values(ascending=False)
    #Find second_highest_salary    
    if len(df) >= 2:
        return pd.DataFrame({'SecondHighestSalary': [df.iloc[1]]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    