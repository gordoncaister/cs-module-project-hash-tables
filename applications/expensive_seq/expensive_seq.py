# Your code here
"""
I dont understand this question

    # if x <= 0:
    #     return y+z
    # else:
    #     return expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y-3,z*2)

function(x,y,z)
    if x is less than or equal to 0:
        return y+z
    else:
        if (x-1,y+1,z) is in dictionary:
            store seperately the value of dictionary[(x-1,y+1,z)]
        else:
            store seperately the value of the function(x-1,y-1,z-1)
            store the value into the dictionary
        if (x-2,y+2,z*2) is in dictionary:
            store seperately the value of dictionary[(x-2,y+2,z*2)]
        else:
            store seperately the value of the function(x-2,y-2,z*2)
            store the value into the dictionary
        if (x-3,y+3,z*3) is in dictionary:
            store seperately the value of dictionary[(x-3,y+3,z*3)]
        else:
            store seperately the value of the function(x-3,y+3,z*3)
            store the value into the dictionary

        save the three stored values added together
        save the above value in my dictionary
        return the above value

"""
values = dict()
# storage = {
#         {(-1,10,40) ,50},
#         {(0,15,20)  ,35}
#     }
def expensive_seq(x, y, z):

    if x <= 0:
        return y+z
    if (x,y,z) in values:
        return values[(x,y,z)]
    else:
        total = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        values[(x,y,z)] = total
        return total
    # else:
    #     if (x-1,y+1,z) in values:
    #         one = values[(x-1,y+1,z)]
    #     else:
    #         one = expensive_seq(x-1,y+1,z)
    #         values[(x-1,y+1,z)] = one
    #     if (x-2,y+2,z*2) in values:
    #         two = values[(x-2,y+2,z*2)]
    #     else:
    #         two = expensive_seq(x-2,y+2,z*2)
    #         values[(x-2,y+2,z*2)] = two
    #     if (x-3,y+3,z*3) in values:
    #         three = values[(x-3,y+3,z*3)]
    #     else:
    #         three = expensive_seq(x-3,y+3,z*3)
    #         values[(x-3,y+3,z*3)] = three
    #     total = one + two + three
    #     values[(x,y,z)]=total
        
    #     return total

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
