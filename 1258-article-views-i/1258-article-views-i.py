import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[views.author_id == views.viewer_id].sort_values('author_id')
    df = df.author_id.to_frame().drop_duplicates()
    df.rename(columns={'author_id': 'id'}, inplace=True)
    return df