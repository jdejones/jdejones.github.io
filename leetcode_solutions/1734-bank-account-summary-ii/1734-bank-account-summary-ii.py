import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions_gb = transactions[['account', 'amount']].groupby(['account']).sum()
    df = users.merge(transactions_gb, how='left', on='account')
    df.rename(columns={'amount': 'balance'}, inplace=True)
    df = df[['name', 'balance']]
    return df[df.balance > 10_000]
