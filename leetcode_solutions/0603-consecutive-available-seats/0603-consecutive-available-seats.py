import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    return (cinema['seat_id'].loc[((cinema.free == 1) & (cinema.free.diff(-1) == 0)) | 
    ((cinema.free == 1) & (cinema.free.diff(1) == 0))]).sort_values().to_frame()
