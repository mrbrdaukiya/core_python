#Access String using Loop

#For Loop
print("For Loop Start")

str1 = "GuruChoudhary"
# for c in str1:
    # print(c)

n = len(str1)

for i in range(n):
    print(str1[i])

print("lenth of string: ", n)    
print()
print("While Loop start")

#While Loop
j = 0
while j < n:
    print(str1[j])
    j += 1
