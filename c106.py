# Nested Function 
def disp():
    def show():
        print("show function")
    print("disp function")
    show()

disp()


print()
print("*************************")
print()

# Nested Function with retrun statement


def disp(st):
    def show():
        return "show function "
    result = show() + st + " Disp Function"
    return result
# a = disp()
# print(a)
print(disp("Guru"))