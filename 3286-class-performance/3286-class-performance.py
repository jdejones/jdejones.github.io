import pandas as pd

def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    scores['total'] = scores[['assignment1', 'assignment2', 'assignment3']].sum(axis=1)
    diff_val = scores['total'].max()- scores['total'].min()
    s = pd.Series(diff_val, name='difference_in_score')
    return s.to_frame()