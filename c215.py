# List Comprehension

# Without List Comprehension

# lst1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

new_lst1 = []
for i in range(20):
    new_lst1.append(i+1)

# print(new_lst1)



# with List Comprehension

# lst2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

new_lst2 = [i+1 for i in range(20)]


# print(new_lst2)


# -------------------------------------------------------------------------------------

lst1 = []

for i in range(21):
    if (i%2==0):
        lst1.append(i)
# print(lst1)

# with List Comprehension
lst2 = [i for i in range(21) if i%2==0]

# print("New List :",lst2)


# -------------------------------------------------------------------------------------

lst1 = []

for i in range(21):
    if (i%2==0):
        if(i%3==0):
            lst1.append(i)
# print("Old List :",lst1)

# with List Comprehension
lst2 = [i for i in range(21) if i%2==0 if i%3==0]

# print("New List :",lst2)


# -------------------------------------------------------------------------------------

lst1 = []

for i in range(11):
    if (i%2==0):
        lst1.append(i)
    else:
        lst1.append("Invalid")
print("Old List :",lst1)
print()


# for i in lst1:
#     print(i)


# with List Comprehension
lst2 = [i if i%2==0 else "Invalid" for i in range(11)]

# for i in lst2:
#     print(i)

print("New List :",lst2)







print()
print("***************************************************************")
print()




# Nested List Comprehension

a = [[24,30,36],[28,35,42]]
for i in range(6,8):
    for j in range(4,7):
        pass

lst = [[i*j for j in range(4,7)] for i in range(6,8)]
print(lst)