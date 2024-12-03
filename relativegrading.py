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



def grade_with_custom_thresholds(df):
    marks_column = 'marks'
    mean = df[marks_column].mean()
    std_dev = df[marks_column].std()

    custom_thresholds = {}
    print("Enter custom Z-score thresholds (lower and upper limits) for each grade in descending order (A+ to D):")
    
    grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D']

    for grade in grades:
        while True:
            try:
                lower_limit = float(input(f"Enter lower Z-score limit for {grade}: "))
                upper_limit = float(input(f"Enter upper Z-score limit for {grade}: "))
                
                if lower_limit >= upper_limit:
                    raise ValueError(f"The lower Z-score limit for {grade} must be less than the upper limit.")
                
                custom_thresholds[grade] = (lower_limit, upper_limit)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid Z-score limits.")
    
    custom_thresholds['F'] = (float('-inf'), float('-inf')) 
    def assign_custom_grade(marks):
        z_score = (marks - mean) / std_dev  
        for grade, (lower_limit, upper_limit) in custom_thresholds.items():
            if lower_limit <= z_score < upper_limit:
                return f'{grade} ({lower_limit} - {upper_limit})'
        return 'F (0.00)'

    df['Grade'] = df[marks_column].apply(assign_custom_grade)
    return df