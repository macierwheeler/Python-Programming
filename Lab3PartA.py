# The file cities_and_times.txt contains city names and times.
# Each line contains the name of the city, followed by the name of the day ("Sun")
# and the time in the form hh:mm.
#
# $ cities_and_times.txt
# Chicago   Sun 01:52
# Columbus Sun 02:52
# Riyadh  Sun 10:52
# Copenhagen  Sun 08:52
# Kuwait City Sun 10:52
# Rome    Sun 08:52
# ...
#
# Write a function summary(day, hour, minute). The function takes the day of week, hour, and
# minute as input, reads the file, find cities that followed by the corresponding time,
# and creates an alphabetically-ordered list of the form:
# [('Ankara', 'Sun', (10, 52)), ('Istanbul', 'Sun', (10, 52)),
# ..., ('Moscow', 'Sun', (10, 52)), ('Riyadh', 'Sun', (10, 52))]
# i.e. City names are in an ascending alphabetical order. The element of the result list
# should be a tuple containing three elements: (<city name>, <day of week>, (<hour>, <minute>)).
# Noted that city names can consist of multiple words like "Salt Lake City".
#
# Input:
# day, hour, minute. Type: string, string, string
#
# Output:
# an alphabetically-ordered list of tuples containing three elements: (<city name>, <day of week>, (<hour>, <minute>))
# Type: (<string>, <string>, (<int>, <int>))
#
# Example:
# summary('Sun', '10','52') =
# [('Ankara', 'Sun', (10, 52)),
# ('Istanbul', 'Sun', (10, 52)),
# ('Kuwait City', 'Sun', (10, 52)),
# ('Moscow', 'Sun', (10, 52)),
# ('Riyadh', 'Sun', (10, 52))]


def summary(day, hour, minute):
    lines = open("/Users/maciewheeler/Downloads/cities_and_times.txt", 'r').readlines()
    lines.sort()
    ###
    myList = []

    for line in lines:
        splitline = line.rstrip().split()
        if day in splitline: # all the lines which have the day as the given day
            time = splitline[-1].split(':')
            if hour == time[0] and minute == time[1]: #all of the lines which have the time
                if (splitline[1] == day):
                    tup = (splitline[0], day, (int(hour), int(minute)))
                    myList.append(tup)
                elif (splitline[2] == day):
                    tup = (splitline[0] + " " + splitline[1], day, (int(hour), int(minute)))
                    myList.append(tup)
                else:
                    tup = (splitline[0] + " " + splitline[1] + " " + splitline[2], day, (int(hour), int(minute)))
                    myList.append(tup)
    myList.sort()
    return myList
    ###


print(summary('Sun', '10', '52'))
