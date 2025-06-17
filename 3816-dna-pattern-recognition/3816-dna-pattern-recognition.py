import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples = samples.assign(has_start=0, has_stop=0, has_atat=0, has_ggg=0)
    samples['has_start'].loc[samples['dna_sequence'].str.contains(r'^ATG', regex=True)] = 1
    samples['has_stop'].loc[samples['dna_sequence'].str.contains(r'(TAA|TAG|TGA)$', regex=True)] = 1
    samples['has_atat'].loc[samples['dna_sequence'].str.contains(r'ATAT', regex=True)] = 1
    samples['has_ggg'].loc[samples['dna_sequence'].str.contains('GGG', regex=True)] = 1
    return samples