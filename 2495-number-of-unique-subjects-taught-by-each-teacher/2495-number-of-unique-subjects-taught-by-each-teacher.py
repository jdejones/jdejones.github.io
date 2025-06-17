import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    tiduniq = teacher.teacher_id.unique()
    subiduniq = [len(teacher.subject_id.loc[teacher.teacher_id == tid].unique()) for tid in tiduniq]
    df = pd.DataFrame({'teacher_id': tiduniq, 'cnt': subiduniq})
    return df