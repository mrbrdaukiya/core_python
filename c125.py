# Pass or Call by Object Raference
def val(x):
    print(x, id(x))
    x = 10 
    print(x, id(x))
    
x = 10
val(x)
print(x, id(x))


print()
print("******************************************************")
print()


def val(lst):
    print("IFBA: ", lst, id(lst))
    lst.append(4)
    print("IFAA:", lst, id(lst))

lst = [1, 2, 3]
print("BCF: ", lst, id(lst))
val(lst)
print("ACF: ", lst, id(lst))


print()
print("******************************************************")
print()


def val(lst):
    print("IFBA: ", lst, id(lst))
    lst = [11, 22, 33]
    print("IFAA:", lst, id(lst))

lst = [1, 2, 3]
print("BCF: ", lst, id(lst))
val(lst)
print("ACF: ", lst, id(lst))


