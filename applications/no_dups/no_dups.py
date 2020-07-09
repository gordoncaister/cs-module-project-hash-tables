def no_dups(s):
    # Your code here
    cache = {}
    sarr = s.split()
    print(sarr)
    for word in sarr:
        if word not in cache:
            cache[word] = None
    
    return " ".join(cache)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))