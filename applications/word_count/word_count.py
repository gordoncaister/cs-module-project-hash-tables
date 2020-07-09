import re
ignorethese = {'"',':',';',',','.','-','+','=','/','\\','|','[',']','{','}','(',')','*','^','&'}

def word_count(s):
    if re.match(r"\w+",s.lower()) is None:
        return {}
    # Your code here
    cache = dict()

    newStr = ''.join(char for char in s if char not in ignorethese)
    print(newStr)
    # for char in ignorethese:
    #     print(char)
    #     newStr = newStr.replace(char,"")
    # print(newStr)
    words = newStr.lower().split()
    for word in words:
        word = word.strip()
        if word != '':
            if word in cache:
                cache[word] += 1
            else:
                cache[word] = 1
        
            
    return cache

if __name__ == "__main__":
    # print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    # print(word_count("Hello    hello"))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))