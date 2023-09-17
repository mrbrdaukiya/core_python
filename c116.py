# Nested Lambda Function
add = lambda x = 10 : (lambda y : x + y)

a = add()
print(a(20))



print()
print("*************************")
print()

# Passing Lambda Function to Another Function

def show(a):
    print(a(8))

show(lambda x : x)


print()
print("*************************")
print()

# Returning Lambda Function 
def add():
    y = 20
    return(lambda x : x +y)

a = add()
print(a(10))