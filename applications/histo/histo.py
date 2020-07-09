# Your code here
from word_count import word_count
with open("robin.txt") as f:
    words = f.read()
totals = word_count(words)

"""
now I have a dictionary of words with their number of occurences as the value
I need to sort the dictionary by key, but replace their values with a number of hashes equal to hash*no instances.

It doesn't matter which order I do these things. I will try do them at the same time.

"""

for i in totals:
    totals[i] = "#"*totals[i]


totals = sorted(totals.items(),key=lambda x: x[1],reverse=True)

for i in totals:
    if len(i[0]) < 7:
        print(i[0],"\t\t\t",i[1])
    elif len(i[0]) >=14:
        print(i[0],"\t",i[1])
    else:
        print(i[0],"\t\t",i[1])

