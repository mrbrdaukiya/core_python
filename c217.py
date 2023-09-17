# Set Comprehension


# set1 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}

new_set1 = set()
for i in range(20):
    new_set1.add(i+1)

# print(new_set1)



# with set Comprehension

# set2 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}

new_set2 = {i+1 for i in range(20)}


# print(new_set2)




# -------------------------------------------------------------------------------------

set1 = set()

for i in range(21):
    if (i%2==0):
        set1.add(i)
# print(set1)

# with set Comprehension
set2 = {i for i in range(21) if i%2==0}

# print("New set :",set2)





# -------------------------------------------------------------------------------------

set1 = set()

for i in range(21):
    if (i%2==0):
        if(i%3==0):
            set1.add(i)
# print("Old set :",set1)

# with set Comprehension
set2 = [i for i in range(21) if i%2==0 if i%3==0]

# print("New set :",set2)



# -------------------------------------------------------------------------------------

# set Comprehension with if else statement


set1 = set()

for i in range(11):
    if (i%2==0):
        set1.add(i)
    else:
        set1.add(i*1000)
# print("Old set :",set1)
print()


# for i in set1:
#     print(i)


# with set Comprehension
set2 = [i if i%2==0 else i*1000 for i in range(11)]

# for i in set2:
#     print(i)

# print("New set :",set2)







print()
print("***************************************************************")
print()




# Nested set Comprehension



st = {(i, j) for j in range(4,7) for i in range(6,8)}
print(st)

print()
print(type(st))