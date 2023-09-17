# Creat an another Nested Dictionary

a = {1 : {'course':'Python', 'fees': 15000}, 2 : {'course':'Javascript', 'fees': 15000}}

for i in a:
    print(i,'= ', a[i])

print()

a[1]['course']= 'Machine Learning'

del a[2]['course']

a[1]['duration'] = '6 Months'

a[3] = {'course':'React JS', 'fees': 15000}


print(a)






print()
print("***************************************************************")
print()



#Accessing Nested Dictionary using For Loop

a = {1 : {'course':'Python', 'fees': 15000}, 2 : {'course':'Javascript', 'fees': 15000}}

print("ID :")
for i in a:
    print(i)

print()



# print("KEYS :")

for id in a:
    for k in a[id]:
        print(k, '= ', a[id][k])

print()

