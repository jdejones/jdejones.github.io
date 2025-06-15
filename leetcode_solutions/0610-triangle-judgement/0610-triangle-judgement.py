import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    
    def triangle_func(df):
        if (df.x + df.y > df.z) and (df.x + df.z > df.y) and (df.y + df.z > df.x):
            return 'Yes'
        else:
            return 'No'
    triangle['triangle'] = triangle.apply(triangle_func, axis=1)
    return triangle
