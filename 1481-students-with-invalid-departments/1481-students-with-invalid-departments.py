import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    df = students[['id', 'name']].loc[~students.department_id.isin(departments.id.to_list())]
    return df