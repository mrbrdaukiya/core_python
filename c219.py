# Dictionary Comprehension


dict1 = {}
for n in range(5):
    dict1[n] = n*2

# print("Old Dictionary :",dict1)



# with Dictionary Comprehension


dict2 = {n:n*2 for n in range(5)}


# print("New Dictionary :",dict2)


# -------------------------------------------------------------------------------------



dict1 = {}
for n in range(10):
    if(n%2==0):
        dict1[n] = n*2

# print("Old Dictionary :",dict1)



# with Dictionary Comprehension


dict2 = {n:n*2 for n in range(10) if n%2==0}


# print("New Dictionary :",dict2)




# -------------------------------------------------------------------------------------



dict1 = {}
for n in range(10):
    if(n%2==0):
        if(n%3==0):
            dict1[n] = n*2

# print("Old Dictionary :",dict1)



# with Dictionary Comprehension


dict2 = {n:n*2 for n in range(10) if n%2==0 if n%3==0}


# print("New Dictionary :",dict2)





# -------------------------------------------------------------------------------------

# Dictionary Comprehension with if else statement


dict1 = {}
for n in range(10):
    if(n%2==0):
        dict1[n] = n
    else:
        dict1[n] = "Invalid"

# print("Old Dictionary :",dict1)



# with Dictionary Comprehension


dict2 = {n:(n if n%2==0 else "Invalid") for n in range(10)}


# print("New Dictionary :",dict2)






# -------------------------------------------------------------------------------------

lst = [(101,'rahul'),(102,'raj')]

dict1 = {k:v for k,v in lst}

print(dict1)

print(type(dict1))