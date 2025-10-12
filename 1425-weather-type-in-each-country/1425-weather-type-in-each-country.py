import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    merged_df = countries.merge(weather, on='country_id')

    df = (
        merged_df.loc[merged_df.day.between('2019-11-01', '2019-11-30', inclusive='both')]
    )

    group = df.groupby('country_name')['weather_state'].mean().reset_index()

    def weather_type(df):
        if df.weather_state <= 15:
            return 'Cold'
        elif df.weather_state >= 25:
            return 'Hot'
        else:
            return 'Warm'
    
    group['weather_type'] = group.apply(weather_type, axis=1)

    return group[['country_name', 'weather_type']]