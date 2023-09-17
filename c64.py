#arange()Function

#syntex numpy 
# from numpy import *
# array_name = arange( start , stop , setpsize, dtype=None)

from numpy import *
a = arange(1, 10,2)
# print(a)

# For Loop
n = len(a)


# for el in a:
#     print(el)

# for el in range(n):
    # print("index",el ,"=", a[el] )



#While Loop
i = 0
while i<n:
    print("index", i,"=",a[i])
    i+=1

