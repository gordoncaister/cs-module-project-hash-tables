# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re
with open("ciphertext.txt") as f:
    words = f.read()

letter_frequency = {}

for i in words:
    if re.match(r"[A-Z]",i):
        if i not in letter_frequency:
            letter_frequency[i] = 1
        else:
            letter_frequency[i] += 1

letter_frequency = dict(sorted(letter_frequency.items(),key=lambda x: x[1],reverse=True))

expected_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U','G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

decrypt_key = {}

for i in range(26):
    decrypt_key[i] = expected_frequency[i]


"""
I need to convert the first dictionary so the values are equal to the keys in the second dictionary

have two lists of letters, one is the frequency in the text, one is the frequency in reality both have 26 letters, one for each letter of the alphabet.
we need to replace each letter in the original string with the value of the key in the expected frequency with the same key as the letter in the letter frequency.

IE. We need to figure out which position in the letter frequency dictionary the current letter is in, find the corresponding value of the key position in the expected frequency and replace the current letter with it.


for each character in the text:
    if the character is not a capital letter we can ignore it:
        find the index of the key that matches the letter in letter frequency
        replace the letter with the key value that matches the above index in expected_frequency

"""
counter = 0
for l in letter_frequency:
    letter_frequency[l] = counter
    counter += 1


print(decrypt_key[letter_frequency[words[33]]])
decoded = ""
for x in range(len(words)):
    if words[x] in letter_frequency:
        print(decrypt_key[letter_frequency[words[x]]], end="")
    else:
        print(words[x],end="")
        
