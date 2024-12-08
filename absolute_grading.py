def grade_with_hec_absolute(df, marks_column='marks'):
    def assign_grade(marks):
        if marks >= 85:
            return 'A'
        elif 80 <= marks < 85:
            return 'A-'
        elif 75 <= marks < 80:
            return 'B+'
        elif 71 <= marks < 75:
            return 'B'
        elif 68 <= marks < 71:
            return 'B-'
        elif 64 <= marks < 68:
            return 'C+'
        elif 61 <= marks < 64:
            return 'C'
        elif 58 <= marks < 61:
            return 'C-'
        elif 54 <= marks < 58:
            return 'D+'
        elif 50 <= marks < 54:
            return 'D'
        else:
            return 'F'

    df['Grade'] = df[marks_column].apply(assign_grade)
    return df


def grade_with_custom_absolute(df, grade_ranges, marks_column='marks', scaling = 0):
    def assign_custom_grade(marks):
        for grade, (lower_limit, upper_limit) in grade_ranges.items():
            if lower_limit <= marks+scaling < upper_limit:
                return grade.replace("_", " ").title()
        return 'F'


    df['Grade'] = df[marks_column].apply(assign_custom_grade)
    return df
