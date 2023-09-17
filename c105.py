# Retrun Statement single value 
# defining a Function

def add(y):
    x = 10
    # y = 20
    # c = x + y
    # return c
    return x + y

# calling a function
sum = add(50)
print(sum)


print()
print("*************************")
print()

# Retrun Statement multiple value 

# defining a Function

def add(y):
    x = 10
    c = x + y
    d = y - x
    return c, d, 50

# calling a function
sum, sub, a = add(50)
print(sum)
print(sub)
print(a)
