import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    exam_counts = (
        examinations
        .groupby('student_id')['subject_name']
        .value_counts()
        .reset_index(name='attended_exams')
    )
    df = (
        students
        .merge(exam_counts, on='student_id')
    )

    stud_sub = students.merge(subjects, how='cross')

    df = df.merge(stud_sub, how='outer').fillna({'attended_exams': 0})

    return df.sort_values(by=['student_id', 'subject_name'])
