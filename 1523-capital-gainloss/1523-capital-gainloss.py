import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    df = stocks.groupby(['stock_name', 'operation'], as_index=False)['price'].sum()
    output_dict = {}
    for name in df.stock_name.unique():
        buy = df['price'].loc[(df.stock_name == name) & (df.operation == 'Buy')].item()
        sell = df['price'].loc[(df.stock_name == name) & (df.operation == 'Sell')].item()
        pnl = sell - buy
        output_dict[name] = pnl
        output_df = pd.DataFrame({'stock_name': list(output_dict.keys()),
                          'capital_gain_loss': list(output_dict.values())})         
    return output_df