# Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, each on a separate line. If the word has an even number of letters, choose the later letter, i.e. the one closer to the end of the string.
# ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Paso Doble'
# 'Viennese Waltz'
# 'Waltz'
# 'Samba'
# 'Rumba'
# 'Tango'
# 'Foxtrot'
# 'Jive'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.



'''sort method for lists allows us to sort using a function which assigns a value to a key that is used for the sort method.'''
''' function that finds middle letter '''
''' main function which sorts the array using the .sort method with the return from our above function as its key '''

"""
sort helper function:
    if the length of the current item % 2 is = 0,
        find the middle character by taking the length of the string dividing that by two, find the (length/2)+1 char.
    if not
        find the middle char by taking the length of the string dividing that by two, find the (length/2) char rounded down
    return the middle character
    
main function: 
    take our array and use sort method passing in the helper function as our key
    for each word in the sorted array:
        print that word

tangos
3

"""

array = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

def sortKey(word):
    middlechar = 0
    if len(word) % 2 == 0:
        middlechar = int(len(word)/2)
        return word[middlechar]
    else:
        middlechar = int(abs(len(word)/2))
        return word[middlechar]
    

array.sort(key=sortKey)
for x in array:
    print(f"{x}")
   
