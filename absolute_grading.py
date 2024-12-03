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


def grade_with_custom_absolute(df, marks_column='marks'):
    custom_thresholds = {}
    print("Enter custom absolute grade thresholds (percentage ranges) for each grade:")

    grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D']
    
    for grade in grades:
        while True:
            try:
                lower_limit = float(input(f"Enter lower limit for {grade}: "))
                upper_limit = float(input(f"Enter upper limit for {grade}: "))
                
                if lower_limit >= upper_limit:
                    raise ValueError(f"The lower limit for {grade} must be less than the upper limit.")
                
                custom_thresholds[grade] = (lower_limit, upper_limit)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid thresholds.")

    custom_thresholds['F'] = (float('-inf'), 50)

    def assign_custom_grade(marks):
        for grade, (lower_limit, upper_limit) in custom_thresholds.items():
            if lower_limit <= marks < upper_limit:
                return f'{grade} ({lower_limit} - {upper_limit})'
        return 'F (0.00)'

    df['Grade'] = df[marks_column].apply(assign_custom_grade)
    return df