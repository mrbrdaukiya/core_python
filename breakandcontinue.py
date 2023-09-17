#Break Statement
for i in range(10):
    print(i)
    if(i == 5):
        break
print("Rest of the Code")

#Continue Statement
for i in range(10):
    if(i == 5):
        continue
    print(i)
print("Rest of the Code")