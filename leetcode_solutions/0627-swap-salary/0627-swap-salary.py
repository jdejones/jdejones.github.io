import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary.sex = salary.apply(lambda x: 'm' if x.sex == 'f' else 'f', axis=1)
    return salary
