# Function return Anothor Function
def disp():
    def show():
        return "show Function"
    print("Disp Function")
    return show
r_sh = disp()
print(r_sh())



print()
print("*************************")
print()

def disp(sh):
    print("Disp Function")
    return sh
def show():
    return "show function"

r_sh = disp(show)
print(r_sh())

# Actual and Formal Argument
# def add(x, y):<--------- = actual argument
#     c = x + y
#     print(c)
# add(10,20)<---------------= formal argument