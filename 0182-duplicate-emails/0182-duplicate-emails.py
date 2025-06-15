import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    repeat = [i for i in person['email'].value_counts().index if person['email'].value_counts()[i] > 1]
    return pd.DataFrame({'Email': repeat})