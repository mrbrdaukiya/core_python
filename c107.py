# Pass a Function as Parameter
def disp(sh):
    print("Disp Function " + sh())

def show():
    return "Show Function"

disp(show)


print()
print("*************************")
print()

def disp(sh):
    return "Disp Function " + sh()

def show():
    return "Show Function"

print(disp(show))