import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    #quality = mean(rating:position)
    #poor_query_% = rating < 3

    group1 = (
        queries
        .groupby('query_name')
        .agg(poor_query_percentage=('rating', lambda x: round(((x < 3).mean() + 1e-10) * 100, 2)))
    )

    queries['qratio'] = queries['rating'] / queries['position']
    group2 = (
        (queries
        .groupby('query_name')['qratio']
        .mean() + 1e-10)
        .round(2)
        .reset_index()
        .rename(columns={'qratio': 'quality'})
    )

    df = group2.merge(group1, on='query_name')

    return df
