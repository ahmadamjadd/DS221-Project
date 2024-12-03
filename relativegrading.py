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
        'D': -2.5,  # Updated threshold for D
        'F': float('-inf')  # F grade for anything below -2.5
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
    print("Enter custom Z-score thresholds for each grade in descending order (A+ to D):")
    
    grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D']

    for grade in grades:
        while True:
            try:
                threshold = float(input(f"Enter Z-score threshold for {grade}: "))
                
                if custom_thresholds and threshold >= max(custom_thresholds.values()):
                    raise ValueError(f"Threshold for {grade} must be less than the previous grade.")
                
                custom_thresholds[grade] = threshold
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid threshold.")
    
    custom_thresholds['F'] = float('-inf') 
    
    df['Grade'] = df[marks_column].apply(lambda marks: next(
        grade for grade, threshold in custom_thresholds.items() 
        if (marks - mean) / std_dev >= threshold
    ))
    return df


