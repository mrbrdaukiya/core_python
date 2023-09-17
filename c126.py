# Function Decorater
def decor(num):
    def inner():
        print("IF: Before enhancing Function")
        num()
        print("IF: After enhancing Function")
    return inner
@decor
def num():
    print("we will use this function")
    print("and will enhance this in decorater")


# num= decor(num)
# num()


print()
print("******************************************************")
print()


def decor(num):
    def inner():
        a = num()
        add = a+5
        return add
    return inner
@decor
def num():
    return 10


# num= decor(num)
# print(num())


print()
print("******************************************************")
print()


def decor1(num):
    def inner():
        b = num()
        multi = b * 5
        return multi
    return inner


def decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner


def num():
    return 10


num= decor(decor1(num))
print(num())