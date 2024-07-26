# In this question, you are given a comma seperated file named occupation.csv under the folder ../resource/asnlib/public,
# which containsthe occupation information and personal data of nearly 1,000 people.
#
# $ head occupation.csv
# user_id,age,gender,occupation,zip_code
# 1,24,M,technician,85711
# 2,53,F,other,94043
# 3,23,M,writer,32067
# ...
#
# The five columns in this table are user id, age, gender,
# occupation and zip code.
#
# Write a function analyze that takes two parameters: minimum and maximum and uses pandas to do the following actions:
# 1. Read the .csv file into a dataframe.
# 2. Calculate the male ratio per occupation by dividing the number of male
# workers by the total number of such workers, and sort the values in descending order i.e., from the most to the least. The ratio should be
# expressed as a percentage, e.g. 40 for 40% or 0.4 or 2/5.
# 3. Given the minimum ratio and a maximum ratio (i.e., the function parameters) return occupations that have a male ratio between
# the two borderlines (i.e., not smaller than the minimum ratio and not greater than the maximum ratio),
# as a list.
#
# INPUT:
# minimum, maximum: minimal male ratio and maximal male ratio. Type: float.
#
# OUTPUT:
# occupations that have a male ratio between the two borderlines, in descending order. Type: list
#
# EXAMPLE:
# analyze(45,55) = ['administrator', 'artist']
#'/Users/maciewheeler/Downloads/occupation.csv'


import pandas as pd


def analyze(minimum, maximum):
    ###
    data = pd.read_csv('../resource/asnlib/public/occupation.csv')
    # apply the function to the gender column and create a new column
    data['gender_new'] = data['gender'].apply(lambda x: 1 if x == 'M' else 0)
    answer = data.groupby('occupation').gender_new.sum() / data.occupation.value_counts() * 100

    # sort to the most male
    answer = answer.sort_values(ascending=False)
    answer = pd.DataFrame(answer, columns=['male_ratio'])

    return list(answer[(answer.male_ratio >= minimum) & (answer.male_ratio <= maximum)].index)
    ###


print(analyze(45, 55))
