def assign_grade(marks):
    if marks >= 85:
        return 'A'
    elif 80 <= marks <= 84:
        return 'A-'
    elif 75 <= marks <= 79:
        return 'B+'
    elif 71 <= marks <= 74:
        return 'B'
    elif 68 <= marks <= 70:
        return 'B-'
    elif 64 <= marks <= 67:
        return 'C+'
    elif 61 <= marks <= 63:
        return 'C'
    elif 58 <= marks <= 60:
        return 'C-'
    elif 54 <= marks <= 57:
        return 'D+'
    elif 50 <= marks <= 53:
        return 'D'
    else:
        return 'F'
    

def generate_grade_report(df):
    new_df = df.copy()
    new_df['grade'] = new_df['marks'].apply(assign_grade)
    return new_df