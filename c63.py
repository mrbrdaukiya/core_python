#Linspace()Function

#syntex numpy 
# from numpy import *
# array_name = logspace( start , stop , nim=50(max) , endpoint= True, base=10.0,dtype=None,axis=0)

from numpy import *
a = logspace(1, 3,5)

# a[2] = 5  
# print(a)

# For Loop
n = len(a)


# for el in a:
    # print(el)

# for el in range(n):
    # print("index",el ,"=", a[el] )


#While Loop
i = 0
while i<n:
    print("index", i,"=",a[i])
    i+=1