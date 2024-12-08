import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy.stats import skew

def make_graphs(df, filename):
    # 1. Histogram of the marks column
    plt.figure(figsize=(10, 6))
    sns.histplot(df['marks'], kde=True, bins=20, color='blue')
    plt.title('Histogram of Marks')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig(f'static/graphs/{filename}_histogram.png')
    plt.close()

    # 2. Boxplot of the marks column
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df['marks'], color='green')
    plt.title('Boxplot of Marks')
    plt.xlabel('Marks')
    plt.savefig(f'static/graphs/{filename}_boxplot.png')
    plt.close()

    # 3. Normalize the marks and create a histogram again
    df['marks_normalized'] = (df['marks'] - df['marks'].mean()) / df['marks'].std()

    
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df['marks_normalized'], kde=True, bins=20, color='purple')
    plt.title('Normalized Histogram of Marks')
    plt.xlabel('Normalized Marks')
    plt.ylabel('Frequency')
    plt.savefig(f'static/graphs/{filename}_normalized_histogram.png')
    plt.close()

    # 4. Bar plot of grades
    plt.figure(figsize=(10, 6))
    grade_counts = df['Grade'].value_counts()
    sns.barplot(x=grade_counts.index, y=grade_counts.values, palette='viridis')
    plt.title('Bar Plot of Number of Grades')
    plt.xlabel('Grades')
    plt.ylabel('Count')
    plt.savefig(f'static/graphs/{filename}_grades_barplot.png')
    plt.close()

    # 5. Calculate and print mean, median, range, std, variance, skewness of marks
    mean_marks = df['marks'].mean()
    median_marks = df['marks'].median()
    range_marks = df['marks'].max() - df['marks'].min()
    std_marks = df['marks'].std()
    variance_marks = df['marks'].var()
    skewness_marks = skew(df['marks'])

    # Save the calculated statistics to a text file
    with open(f'static/graphs/{filename}_statistics.txt', 'w') as f:
        f.write(f'Mean of Marks: {mean_marks}\n')
        f.write(f'Median of Marks: {median_marks}\n')
        f.write(f'Range of Marks: {range_marks}\n')
        f.write(f'Standard Deviation of Marks: {std_marks}\n')
        f.write(f'Variance of Marks: {variance_marks}\n')
        f.write(f'Skewness of Marks: {skewness_marks}\n')