import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    if len(request_accepted) == 0:
        return pd.DataFrame({'accept_rate': [0.00]})
    friend_request = friend_request[['sender_id', 'send_to_id']].drop_duplicates()
    request_accepted = request_accepted[['requester_id', 'accepter_id']].drop_duplicates()
    ratio = round(len(request_accepted) / len(friend_request), 2)
    return pd.DataFrame({'accept_rate': [ratio]})