import pandas as pd

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    group = (
        project.groupby('project_id')['employee_id']
        .nunique()
        .reset_index()
    )
    max_val = group.employee_id.max()
    df = group.loc[group.employee_id == max_val]
    return df.project_id.to_frame()