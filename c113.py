# Variable Lenth Arguments
def add(*num):
    z = num[0] + num[1] + num[2] + num[3] 
    print("Addition :" , z)

add(10, 20, 30, 40)



print()
print("*************************")
print()

# Keyword Variable Lenth Arguments
def add(**num):
    z = num['a'] + num['b'] + num['c']  
    print("Addition :" , z)

add(a = 10 ,b = 20, c = 30)

