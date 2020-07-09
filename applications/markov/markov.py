import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

"""
Go through each word,
    If it is in the cache:
        then take the word immediately after it and add it to they key in the cache as a value
    if not:
        add that as a key to the cache
        set the word immediately after as the value
"""

# TODO: analyze which words can follow other words
# Your code here
cache = {}
words = words.replace("\n"," ")
wordarr = words.split(" ")
for i in range(len(wordarr)):
    if wordarr[i] in cache:
        if i != len(wordarr)-1:
            cache[wordarr[i]].append(wordarr[i+1].strip())
    else:
        if i != len(wordarr)-1:
            cache[wordarr[i]] = [wordarr[i+1]]

print(len(cache))

"""

while iterator is less than 5:
    randomly choose a key:
    if the key is a start word:
        if the key is a stop word:
            print the key
            increment iterator
            print new line
        else:
            print the key
            while condition is not met:
                store a random word from the key's list of followers
                change the key to the random word
                print the random word
                    if the key is an end word:
                        increment iterator
                        print new line
                        meet the condition
    else:
        restart

"""
# TODO: construct 5 random sentences
# Your code here
p = 0
while p < 5:
    key = random.choice(list(cache.keys()))
    if re.match(r'"?[A-Z]',key) != None:
        if re.match(r'[a-zA-Z]+[.?!]"?',key) != None:
            print(key, end="\n\n")
            p +=1
        else:
            print(key, end=" ")
            key = random.choice(list(cache[key]))
            stop = False
            while not stop:
                if re.match(r'[a-zA-Z]+[.?!]"?',key) != None:
                    print(key, end="\n\n")
                    p +=1
                    stop = True
                else:
                    print(key, end=" ")
                    key = random.choice(list(cache[key]))




        
# while p < 5:
#     print("MAIN WHILE\n\n\n\n",p)
#     key = random.choice(list(cache.keys()))
#     if re.match(r'"?[A-Z]',key) != None:
#         print("First if: ", p)
#         if re.match(r'[.?!]"?',key) != None:
#             print("second if: ", p)
#             p += 1
#         else:
#             print("First else:", p)
#             key = random.choice(list(cache[key]))
#             stop = False
#             while not stop:
#                 print("Got here:",key)
#                 if re.match(r'[.?!]"?',key) != None:
#                     print("Third if: ", p)
#                     p += 1
#                     stop = True
#                 else:
#                     key = random.choice(list(cache[key]))
#                     print("First else:",p)
#                     stop = False
#             print("Do I ever Get here?")
#             p += 1

# print(re.match(r'[a-zA-Z]+[.?!]"?','bone."'))