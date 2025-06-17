import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content.rename(columns={'content_text': 'original_text'}, inplace=True)
    user_content['converted_text'] = user_content['original_text'].str.title()
    return user_content
