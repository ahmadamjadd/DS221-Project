## Introduction
This report details the implementation of a comprehensive grading system that supports both absolute and relative grading methodologies. The system is designed to provide instructors with flexibility in grade assignment while maintaining statistical validity and fairness. Our implementation includes data visualization tools, statistical analysis capabilities, and both fixed and customizable grading schemes.

## 1. Introduction
### 1.1 Project Overview
The academic grading system developed in this project addresses the need for a flexible, statistically sound approach to student evaluation. The system supports both absolute grading (based on fixed thresholds) and relative grading (based on statistical distribution of scores), allowing instructors to choose the most appropriate method for their course context.

### 1.2 Objectives
- Implement both absolute and relative grading methodologies
- Provide statistical analysis of grade distributions
- Generate meaningful visualizations for grade analysis
- Ensure compliance with HEC grading guidelines
- Create a user-friendly interface for grade management

## 2. Methodology
### 2.1 Data Input and Processing
The system accepts student data through CSV files with a standardized format containing three essential columns:
- Student Name
- Registration Number
- Marks

Input validation ensures data integrity and proper formatting before processing.

### 2.2 Grading Algorithms

#### 2.2.1 Absolute Grading Implementation
The absolute grading system implements two approaches:

1. HEC Standard Thresholds:
```python
A  : >= 85
A- : 80-84
B+ : 75-79
B  : 71-74
B- : 68-70
C+ : 64-67
C  : 61-63
C- : 58-60
D+ : 54-57
D  : 50-53
F  : < 50
```

2. Custom Thresholds:
The system allows instructors to define custom grade boundaries while maintaining the hierarchical structure of grades.

#### 2.2.2 Relative Grading Implementation
The relative grading system uses statistical measures to assign grades:

1. HEC Standard Method:
- Utilizes z-scores for grade assignment
- Grade boundaries based on standard deviations from the mean:
  ```
  A+ : z ≥ 2.00
  A  : z ≥ 1.50
  A- : z ≥ 1.00
  B+ : z ≥ 0.50
  B  : z ≥ -0.50
  B- : z ≥ -1.00
  C+ : z ≥ -1.33
  C  : z ≥ -1.67
  C- : z ≥ -2.00
  D  : z ≥ -2.50
  F  : z < -2.50
  ```

2. Custom Distribution:
Allows instructors to specify custom z-score boundaries for grade assignment.

## 3. Statistical Analysis
### 3.1 Descriptive Statistics
The system calculates and reports key statistical measures:
- Mean
- Median
- Range
- Standard Deviation
- Variance
- Skewness

### 3.2 Distribution Analysis
The system generates multiple visualizations to analyze grade distributions:

1. Original Grade Distribution

2. Normalized Distribution

3. Grade Category Distribution

4. Score Distribution Analysis

## 4. Results and Analysis
### 4.1 Grade Distribution Comparison
The system provides comparative analysis between original and adjusted grades:

### 4.2 Statistical Insights
Key findings from the statistical analysis:
- Distribution shape and characteristics
- Impact of grading method on final grades
- Identification of outliers and their treatment
- Effectiveness of grade normalization

## 5. System Features
### 5.1 Web Interface
- File upload functionality for grade data
- Interactive selection of grading methods
- Custom threshold definition interface
- Visualization display
- Results download capability

### 5.2 Error Handling
The system implements robust error handling for:
- Invalid file formats
- Missing data
- Incorrect data types
- Out-of-range values
- Invalid grade threshold definitions

## 6. Conclusion
The implemented grading system successfully meets the project requirements by providing:
- Flexible grading methodologies
- Statistical validity in grade assignment
- Comprehensive visualization tools
- User-friendly interface
- Robust error handling

The system's ability to handle both absolute and relative grading schemes, coupled with its statistical analysis capabilities, makes it a valuable tool for academic grade management.

## 7. Future Enhancements
Potential improvements for future iterations:
- Additional statistical methods for grade adjustment
- Enhanced visualization options
- Batch processing capabilities
- Integration with learning management systems
- Extended reporting capabilities

## 8. Collaborators
The project was developed with contributions from:
- Muhammad Ahmad Amjad
- [Abdullah Ejaz Janjua](https://github.com/abdullahejazjanjua)

## Appendix A: Technical Implementation Details
### A.1 Dependencies
- Python 3.x
- Flask (Web Framework)
- Pandas (Data Processing)
- NumPy (Numerical Computations)
- Matplotlib/Seaborn (Visualization)
- SciPy (Statistical Calculations)

### A.2 Key Functions
```python
# Grade assignment functions
grade_with_hec_absolute()
grade_with_custom_absolute()
grade_with_hec_thresholds()
grade_with_custom_relative()

# Visualization functions
make_graphs()

# Utility functions
create_zip()
```

