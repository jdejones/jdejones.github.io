import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee.team_id.value_counts().to_frame('team_size').reset_index()
    df = employee.merge(counts, how='left', on='team_id')
    return df[['employee_id', 'team_size']]
