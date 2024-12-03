def grade_with_hec_thresholds(df):
    marks_column = 'marks'
    mean = df[marks_column].mean()
    std_dev = df[marks_column].std()

    hec_thresholds = {
        'A+': 2,
        'A': 1.5,
        'A-': 1,
        'B+': 0.5,
        'B': -0.5,
        'B-': -1,
        'C+': -1.33,
        'C': -1.67,
        'C-': -2,
        'D': -2.5, 
        'F': float('-inf') 
    }

    df['Grade'] = df[marks_column].apply(lambda marks: next(
        grade for grade, threshold in hec_thresholds.items() 
        if (marks - mean) / std_dev >= threshold
    ))
    return df



def grade_with_custom_relative(df, grade_ranges, marks_column='marks'):
    mean = df[marks_column].mean()
    std_dev = df[marks_column].std()

    def assign_custom_grade(marks):
        z_score = (marks - mean) / std_dev 
        for grade, (lower_limit, upper_limit) in grade_ranges.items():
            if lower_limit <= z_score < upper_limit:
                return f'{grade.replace("_", " ").title()} ({lower_limit} - {upper_limit})'
        return 'F'

    df['Grade'] = df[marks_column].apply(assign_custom_grade)
    return df
