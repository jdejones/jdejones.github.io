import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    posts = submissions.loc[submissions.parent_id.isnull()].drop_duplicates()
    comments = submissions.loc[submissions.parent_id.notnull()].drop_duplicates()
    
    counts = comments.parent_id.value_counts().reset_index()
    
    df = posts.merge(counts, how='left', left_on='sub_id', right_on='parent_id')
    df = df.rename(columns={'sub_id': 'post_id', 'count': 'number_of_comments'})
    df = df[['post_id', 'number_of_comments']].sort_values('post_id').fillna(0)

    return df
