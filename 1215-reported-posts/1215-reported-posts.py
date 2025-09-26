import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    df = (
        actions
        .loc[(actions.action_date == '2019-07-04') 
            & (actions.action == 'report')]
        .dropna(subset='extra')
        .drop_duplicates(subset=['post_id', 'action_date', 'extra'])
    )
    df = (
        df
        .value_counts('extra')
        .reset_index()
    )

    group = (
        df
        .groupby('extra')['count']
        .sum()
        .reset_index()
    )
    group = (
        group
        .rename(columns={'extra': 'report_reason', 'count': 'report_count'})
    )

    return group[['report_reason', 'report_count']]
    #return df