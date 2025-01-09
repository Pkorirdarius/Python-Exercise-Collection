"""
    Manipulation of mathematical functions using numpy to simplify calculations
"""
# importing numpy for mathematical operations
import numpy as np
# defining grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
#Use numpy functions to calculate the mean, median, and standard deviation of the grades.
# mean
grade_mean = grades.mean()
print(f"The grades mean is :{grade_mean}")
# median
grade_median = np.median(grades)
print(f"The median of the array is :{grade_median}")
# standard deviation
grade_std = grades.std()
print(f"The standard deviation of the grades is :{grade_std}")
# maximum grade
max_grade = grades.max()
print(f"The maximum grade is :{max_grade}")
# minimum grade
min_grade = grades.min()
print(f"The minimum grade is {min_grade}")
# sort the grades in ascending order
arranged_grades = grades.sort()
print(f"the sorted grades are:{arranged_grades}")
# index of highest grade
highest_grade = np.argmax(grades)
print(f"The index of the highest grade is : {highest_grade}")
# Use np function to count students who scored 90
count_above_90 = np.sum(grades > 90)
print(f"The count of students who scorded above 90 is :{count_above_90}")
# calculate the percentage of students who scored above 90
total_students = len(grades)
percentage_above_90 = (count_above_90/total_students)* 100
print(f"Percentage of students who scored above 90: {percentage_above_90:.2f}%")
# calculate the percentage of students who scored below 75
count_below_75 = np.sum(grades < 75)
percentage_below_75 = (count_below_75/total_students)* 100
print(f"Percentage of students who scored below 75: {percentage_below_75:.2f}%")
# extract all the grades above 90 
high_performers = grades[grades > 90]
print(f"High performers : {high_performers}")
# Create a new array called "passing_grades" that contains all the grades above 75. Print the result of all the above
passing_grades = grades[grades > 75]
print(f"Passed grades : {passing_grades}")

