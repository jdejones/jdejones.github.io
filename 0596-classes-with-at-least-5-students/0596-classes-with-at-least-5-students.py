import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].apply(lambda x: len(x.sum())).reset_index()
    return df.loc[df['student'] >= 5, 'class'].to_frame()