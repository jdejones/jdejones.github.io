import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets['tweet_id'].loc[tweets['content'].str.len() > 15].to_frame()
