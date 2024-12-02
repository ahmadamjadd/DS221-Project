def assign_grade(marks):
    if marks >= 85:
        return 'A (3.67 - 4.00)'
    elif 80 <= marks <= 84:
        return 'A- (3.34 - 3.66)'
    elif 75 <= marks <= 79:
        return 'B+ (3.01 - 3.33)'
    elif 71 <= marks <= 74:
        return 'B (2.67 - 3.00)'
    elif 68 <= marks <= 70:
        return 'B- (2.34 - 2.66)'
    elif 64 <= marks <= 67:
        return 'C+ (2.01 - 2.33)'
    elif 61 <= marks <= 63:
        return 'C (1.67 - 2.00)'
    elif 58 <= marks <= 60:
        return 'C- (1.31 - 1.66)'
    elif 54 <= marks <= 57:
        return 'D+ (1.01 - 1.30)'
    elif 50 <= marks <= 53:
        return 'D (0.10 - 1.00)'
    else:
        return 'F (0.00)'
    

def generate_grade_report(df):
    new_df = df.copy()
    new_df['grade'] = new_df['marks'].apply(assign_grade)
    return new_df