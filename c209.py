# Nested Dictionary

# disk = {"a":{},
#         "b": ""}
# print(disk)
# print(type(disk))

a = {
    'course': 'python', 'fees': 15000, 1:{'course': 'javascript', 'fees':10000}
}
print(a[1]['fees'])
a['course'] = 'Machin lerning'
# del a[1]['course']
a[1]['fees'] = 200000
print(a)

print()

a[1][2] = {'course':'reacrjs', 'fees': 3000}
print(a)





print()
print("***************************************************************")
print()



#Accessing Nested Dictionary using For Loop

a = {'course': 'python', 'fees': 15000, 1:{'course': 'javascript', 'fees':10000}}

for i in a:
    print(i, '=',a[i])

print()
print()



for i in a:
    if type(a[i]) is dict:
        for k in a[i]:
            print(k, '= ', a[i][k])
    else:
        print(i, '= ',a[i])