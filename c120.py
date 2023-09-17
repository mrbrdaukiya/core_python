# Local Variables
def add(y):
    x = 10
    print(x)
    print(x + y)

add(10)
# print(x)  <------------------XXXX




print()
print("*************************")
print()

# Global Variables
a = 50
def show():
    x = 10
    print(a)
    print(x)
show()
print("Global Variables :", a)



print()
print("*************************")
print()

# Global Keyword
a = 50
def show():
    a = 10
    print("A :",a)

show()
print("A :",a)


print()
print("*************************")
print()

i = 50
def show():
    global i
    i = i + 1
    print("I :",i)

show()
print("I :",i)



print()
print("*************************")
print()


j = 0
def guru():
    # global j
    j = 0 
    while j < 5:
        j += 1
        print(j)

guru()

