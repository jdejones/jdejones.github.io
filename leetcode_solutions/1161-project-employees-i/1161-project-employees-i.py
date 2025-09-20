import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee, how='left', on='employee_id')
    df = (
    df.groupby('project_id')['experience_years']
    .mean()
    .round(2)
    .reset_index())
    df = df.rename(columns={'experience_years': 'average_years'})
    return df
