# Passing Tuple to Function

def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)

tup = (10, 20, 30, "Guru")
show(tup)



print()
print("*****************************************************")
print()



# Passing and Returning Tuple

def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)
    return t

tup = (10, 20, 30, "Guru")
new_tup = show(tup)
print(new_tup)
print(type(new_tup))