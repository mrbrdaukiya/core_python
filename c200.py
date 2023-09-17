# items() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print("Original dict : ")
print(student)
print()

it = student.items()

print(it)
print(type(it))

print()

lst = list(it)

print(lst)
print(type(lst))
print()


print(lst[0])
print(lst[0][0])
print(lst[0][1])

print()

for i in lst:
    for c in i:
        print(c)



print()
print("***************************************************************")
print()


# keys() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print("Original dict : ")
print(student)
print()

all_keys = student.keys()

print(all_keys)
print(type(all_keys))

print()


keys_lst = list(all_keys)

print(keys_lst)
print(type(keys_lst))
print()

print(keys_lst[0])
print(keys_lst[1])
print(keys_lst[2])

print()

for k in keys_lst:
    print(k)



print()
print("***************************************************************")
print()


# values() Method in Dictionary

student = {101 : "rahul", 102 : "sonam", 103 : "raj"}

print(id(student))
print("Original dict : ",student)
print()

all_value = student.values()

print(all_value)
print(type(all_value))

print()

value_lst = list(all_value)
print(value_lst)
print(type(value_lst))

print()

for i in value_lst:
    print(i)