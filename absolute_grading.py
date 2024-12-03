def grade_with_hec_absolute(df, marks_column='marks'):
    def assign_grade(marks):
        if marks >= 85:
            return 'A (3.67 - 4.00)'
        elif 80 <= marks < 85:
            return 'A- (3.34 - 3.66)'
        elif 75 <= marks < 80:
            return 'B+ (3.01 - 3.33)'
        elif 71 <= marks < 75:
            return 'B (2.67 - 3.00)'
        elif 68 <= marks < 71:
            return 'B- (2.34 - 2.66)'
        elif 64 <= marks < 68:
            return 'C+ (2.01 - 2.33)'
        elif 61 <= marks < 64:
            return 'C (1.67 - 2.00)'
        elif 58 <= marks < 61:
            return 'C- (1.31 - 1.66)'
        elif 54 <= marks < 58:
            return 'D+ (1.01 - 1.30)'
        elif 50 <= marks < 54:
            return 'D (0.10 - 1.00)'
        else:
            return 'F (0.00)'

    df['Grade'] = df[marks_column].apply(assign_grade)
    return df


def grade_with_custom_absolute(df, grade_ranges, marks_column='marks'):
    def assign_custom_grade(marks):
        for grade, (lower_limit, upper_limit) in grade_ranges.items():
            if lower_limit <= marks < upper_limit:
                return f'{grade.replace("_", " ").title()} ({lower_limit} - {upper_limit})'
        return 'F (0.00)'  

    df['Grade'] = df[marks_column].apply(assign_custom_grade)
    return df




import pandas as pd

# Example DataFrame
df = pd.DataFrame({'marks': [90, 82, 73, 58, 47]})

# Example of grade ranges for absolute grading (percentage-based)
grade_ranges_absolute = {
    'A_plus': (85, 100),
    'A': (80, 85),
    'A_minus': (75, 80),
    'B_plus': (71, 75),
    'B': (68, 71),
    'B_minus': (64, 68),
    'C_plus': (61, 64),
    'C': (58, 61),
    'C_minus': (54, 58),
    'D': (50, 54)
}

# Example of grade ranges for relative grading (Z-score based)
grade_ranges_relative = {
    'A_plus': (1.5, 2.5),
    'A': (1, 1.5),
    'A_minus': (0.5, 1),
    'B_plus': (0, 0.5),
    'B': (-0.5, 0),
    'B_minus': (-1, -0.5),
    'C_plus': (-1.33, -1),
    'C': (-1.67, -1.33),
    'C_minus': (-2, -1.67),
    'D': (-2.5, -2)
}

# Apply the custom absolute grading function
df_with_absolute_grades = grade_with_custom_absolute(df, grade_ranges_absolute)
print("Absolute Grading:")
print(df_with_absolute_grades)

# Apply the custom relative grading function
# df_with_relative_grades = grade_with_custom_relative(df, grade_ranges_relative)
# print("\nRelative Grading:")
# print(df_with_relative_grades)

