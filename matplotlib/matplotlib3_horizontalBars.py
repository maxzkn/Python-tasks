import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# ----------- READ CSV FILE - METHOD 1 - USING CSV MODULE FROM STANDARD LIBRARY ------------

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file) # creates a dictionary where we can access values by keys, not indexes like in list
#
#     # -- DON'T NEED THIS --
#     # row = next(csv_reader) # grab first line from csv reader
#     # print(row)
#     # print(row['LanguagesWorkedWith']) # they are delimited by semicolons, we can split them on semicolons and create a list
#     # print(row['LanguagesWorkedWith'].split(';')) # a list of languages
#     # -- --
#
#     # now we need to count the languages, so we will use Counter method from collections library:
#     language_counter = Counter()
#
#     for row in csv_reader:  # loop through every row in csv_reader
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))  # update counter with a list of languages for every single row
#
# # -- DON'T NEED THIS --
# # print(language_counter)  # a list with languages and counters
# # print(language_counter.most_common(15))  # returned list and each item is a tuple with 15 languages and count
# # -- --
#
# # let's plot this data (we need to split languages to their own list and counts to their own list):
#
# languages = []
# popularity = []
#
# for item in language_counter.most_common(15):  # loop over each tuple in a list
#     languages.append(item[0])  # first value in tuples are languages
#     popularity.append(item[1])  # second values in tuples are counters
#
# print(languages)  # list with langs
# print(popularity)  # list with counts
#
# languages.reverse()
# popularity.reverse()
#
# plt.barh(languages, popularity)  # bar is difficult to see the x labels, so we use barh for horizontal bars
#
# plt.title("Most popular languages")
# # plt.ylabel("Languages")
# plt.xlabel("Number of people who use")
#
# plt.tight_layout()
#
# plt.show()


# ----------- READ CSV FILE - METHOD 2 - USING PANDAS AND READCSV METHOD (FASTER WAY) -------------

data = pd.read_csv('data.csv')  # read csv file with pandas and save to variable 'data'
# specify columns:
ids = data['Responder_id']  # save to ids variable all of the data under Responder_id column
lang_responses = data['LanguagesWorkedWith']  # save to lang_responses variable all of the data under LanguagesWorkedWith column

# now we need to count the languages, so we will use Counter method from collections library:
language_counter = Counter()

for response in lang_responses:  # loop through every row in csv_reader
    language_counter.update(response.split(';'))  # update counter with a list of languages for every single row

# let's plot this data (we need to split languages to their own list and counts to their own list):

languages = []
popularity = []

for item in language_counter.most_common(15):  # loop over each tuple in a list
    languages.append(item[0])  # first value in tuples are languages
    popularity.append(item[1])  # second values in tuples are counters

print(languages)  # list with langs
print(popularity)  # list with counts

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)  # bar is difficult to see the x labels, so we use barh for horizontal bars

plt.title("Most popular languages")
# plt.ylabel("Languages")
plt.xlabel("Number of people who use")

plt.tight_layout()

plt.show()