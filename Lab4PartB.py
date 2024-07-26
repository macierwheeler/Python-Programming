# You are given a file  containing data for the employees of a company for their payroll. A sample of the
# data contained in the file is given in sample.csv, available at ./resource/asnlib/public/docs/sample.csv. It has
# four columns: date, employee, department and hours, where hours column records the number of hours (a float) the
# respective employee worked for at the recorded date (first column).
# There are four departments: ADMIN, SALES, SHIP and TECH.
#
# You are required to write a function read_data(filename, employee, dept, hrs_worked) which uses pandas
# to do the following:
# 1. read the file pointed to by the filename
# 2. find all the records of the employee when they worked in the dept department, and the number of hours they worked
#    is at least hrs_worked
# 3. return the records found in 2. as a pandas DataFrame
#
# function read_data(filename, employee, dept, hrs_worked)
# Inputs: 4 inputs
#   - filename  : name of the file to be read, type string
#   - employee  : name of employee, type string
#   - dept      : department as in the employees.csv file, type string
#   - hrs_worked: items_sold as in the sales.csv file, type float
#
# Outputs:
#   - a pandas DataFrame
# "/Users/maciewheeler/Downloads/sample.csv"


import pandas as pd


def read_data(filename, employee, dept, hrs_worked):
    ###
    data = pd.read_csv(filename)
    answer = data[(data.employee == employee) & (data.department == dept) & (data.hours >= hrs_worked)]
    return answer
    ###


print(read_data("sample.csv", "Tony", "SALES", 2.8))
