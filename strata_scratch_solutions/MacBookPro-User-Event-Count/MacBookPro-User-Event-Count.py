# Import your libraries
import pandas as pd

# Start writing code
df = playbook_events.event_name.loc[playbook_events.device == 'macbook pro'].value_counts()

df = df.reset_index()

df.columns = ['event_name', 'event_count']

return df
