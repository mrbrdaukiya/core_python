#Recursion
def show():
    print("Guru Choudhary")
    # show()
show()



print()
print("*************************")
print()


i = 0
def show():
    global i
    i =i+1
    print("My Function", i)
    # show()
show()


print()
print("*************************")
print()

import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())
