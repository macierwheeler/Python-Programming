# This question shall make use of a file similar to the sample.csv
# You are required to write a function summary(filename, employee, dept) which uses pandas to do the following:
# 1. read the file pointed to by the filename
# 2. filters the data read in 1. by the employee and the department (dept) passed as argument
# 3. finds the mean, median, maximum and minimum of the hours worked for the
#    data rows computed in 2. using appropriate Pandas functions
# 4. returns the quantities found in 3. above in the same order
#
# function summary(filename, employee, dept)
# Inputs: 3 inputs
#   - filename: the file to be read, type string
#   - employee: the name of an employee, type string
#   - dept    : the name of a department, type string
#
# Outputs: a tuple of four numbers
#   mean, median, maximum and minimum of the hours worked for the employee working in the department passed as inputs
# "/Users/maciewheeler/Downloads/sample.csv"


import pandas as pd


def summary(filename, employee, dept):
    ###
    data = pd.read_csv(filename)
    rows = data[(data.employee == employee) & (data.department == dept)]
    mean = rows.hours.mean()
    median = rows.hours.median()
    maximum = rows.hours.max()
    minimum = rows.hours.min()

    tup1 = (mean, median, maximum, minimum)
    return tup1
    ###


print(summary("sample.csv", "Tony", "SALES"))
