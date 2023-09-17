# Passing List to Function

def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)

lst = [10, 20, 30, "Guru Choudhary"]
show(lst)

print()
print("******************************************************************")
print()

# Passing and Returning List to Function

def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)
    return l

lst = [10, 20, 30, "Guru Choudhary"]
new_lst = show(lst)
print()
print(new_lst)
print(type(new_lst))