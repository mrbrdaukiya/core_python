#Function
#type - 2
# 1) Built-in Function -------------print(), upper().....etc
# 2) User-defined Function -------------made by User

# syntex--

# function body( type -1)
#           def Function_name():
#                    Local variable
#                    block of statement
#                    return(variable or expression)

# function body( type -2)
#           def Function_name(para1 , para2,............):
#                    Local variable
#                    block of statement
#                    return(variable or expression)
#                    note :- Need to maintain proper Indentation

# defining a Function

def disp():
    name = "Guru Choudhary"
    print("My Name is ", name,)

#Calling a Function

disp()
disp()
disp()

print()
print("*************************")
print()

#Defining Function
def add():
    x = 10
    y = 20
    c = x + y
    # z = y + x + 10
    print(c)

add()

def sub():
    x = 10
    y = 20
    c = y - x
    print(c)

sub()


print()
print("*************************")
print()


#Function without Argument and Parameter

def add():
    x = 10
    y = 20
    c = x + y
    print(c)

#calling function without argument

add()



print()
print("*************************")
print()

#Function with Argument and Parameter

def add(y):
    x = 10
    c = x + y
    print(c)

#calling function without argument

add(20.88)


print()
print("*************************")
print()

def add(y):
    print(y)

add("guru")




print()
print("*************************")
print()

#Function with Argument and Parameter

def add(y):
    x = 10.54849316
    print( x + y)
    print(f"Formatted Output {x + y:5.2f}")

#calling function without argument

add(20)