# Keyword Arguments
def show(name, age):
    # print(name, age)
    print(f"Name : {name} and Age : {age}.")

show(age = 26 ,name = "Guru Choudhary" )


print()
print("*************************")
print()


# Default Arguments

def show(name , age = 27):
    print(f"Name : {name} and Age : {age}.")

# show(name = "Guru Choudhary", age = 62 )
show(name = "Guru Choudhary")