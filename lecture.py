import math
inv_sqrt = {}
def build_lookup_table():
    for i in range(1,1000):
        inv_sqrt[i] = 1/math.sqrt(i)
build_lookup_table()
print(inv_sqrt[4])
print(inv_sqrt[22])
print(inv_sqrt[36])