import csv

# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values?rq=1
# NaN (not a number)
print(float("nan"))

# Data Set QUESTION 4 OF 8
# How many NEOs have IAU names in the data set?
# Hint: Count the number of rows that have nonempty entries in the "name" column.
with open("data/neos.csv", "r") as infile:
    reader = csv.DictReader(infile)
    count = 0
    for row in reader:
        # print(row)
        if row["name"]:
            count += 1
    print(count)

# ADDITION - UDACITY ANSWER:
# def load_neos(neo_csv_path='data/neos.csv'):
#   # store number of all neos
#   count_all = 0
#   # store number of neos with nonempty name
#   count_nonempty = 0
#   with open(neo_csv_path, 'r') as infile:
#     reader = csv.DictReader(infile)
#     for row in reader:
#       count_all += 1
#       if row['name']:
#         count_nonempty += 1
#
#   return count_all, count_nonempty
#
#
# print(load_neos())  # output: (23967, 343)

# QUESTION 5 OF 8
# How many NEOs have diameters in the data set?
#
# Hint: Count the number of rows that have nonempty entries in the "diameter" column.
with open("data/neos.csv", "r") as infile:
    reader = csv.DictReader(infile)
    count = 0
    for row in reader:
        # print(row)
        if row["diameter"]:
            count += 1
    print(count)

# QUESTION 6 OF 8
# How many close approaches are in the cad.json data set?
# Hint: Instead of manually counting the entries, you can use the value of the "count" key.

import json

with open("data/cad.json") as jasoninput:
    contents = json.load(jasoninput)
    print(contents["count"])

# QUESTION 7 OF 8
# On January 1st, 2000, how close did the NEO whose primary designation is "2015 CL" pass by Earth?
# Hint: Find entries whose date starts with '2000-Jan-01'.
# One of the lists represents the close approach of the NEO "2015 CL".
# What is the value corresponding to the distance from Earth?
with open("data/cad.json") as jasoninput:
    contents = json.load(jasoninput)
    data = contents["data"]
    for d in data:
        if d[3].startswith("2000-Jan-01") and d[0] == "2015 CL":
            print(d[4])

# QUESTION 8 OF 8
# On January 1st, 2000, how fast did the NEO whose primary designation is "2002 PB" pass by Earth?
# Hint: Find entries whose date starts with '2000-Jan-01'.
# One of the lists represents the close approach of the NEO "2002 PB".
# What is the value corresponding to the velocity relative to Earth?

with open("data/cad.json") as input:
    contents = json.load(input)
    data = contents["data"]
    for d in data:
        if d[3].startswith("2000-Jan-01") and d[0] == "2002 PB":
            print(d[-4])
