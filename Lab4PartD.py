# This question shall make use of a file similar to the sample.csv
#
# Given an employee and a specific department, sometimes the company might be interested in finding out
# what percentage of the total hours worked by that employee in that department by the date the employee worked on.
# E.g. if the total number of hours worked by an employee in say the TECH department were 80, and on 6/14/2019 the
# employee worked for 6 hours in the TECH department, then the percentage of hours worked in TECH on 6/14/2019 by the
# employee = 6/80 * 100 = 7.5%
#
# You are required to write a function hours_proportion(filename, employee, dept) which uses Pandas to do the following:
# 1. read the file pointed to by the filename
# 2. use the map operation with the lambda function to compute the percentage of total hours worked by the employee in
#    the department (dept) on each of the day the employee worked in that specific department
# 3. returns the percentage hours at all recorded times for the city found in 2. as a Pandas series
#
# function hours_proportion(filename, employee, dept)
# Inputs: 3 inputs
#   - filename: the file to be read, type string
#   - employee: the name of the employee, type string
#   - dept    : the name of the department, type string
#
# Outputs: One output
#   the percentage of hours worked in the department on each of the day the employee worked there, type pandas series
# "/Users/maciewheeler/Downloads/sample.csv"


import pandas as pd


def hours_proportion(filename, employee, dept):
    ###
    data = pd.read_csv(filename)
    rows = data[(data.employee == employee) & (data.department == dept)]
    hours_sum = rows.hours.sum()
    return rows.hours.map(lambda x: x / hours_sum * 100)
    ###


print(hours_proportion("sample.csv", "Tony", "SALES"))
