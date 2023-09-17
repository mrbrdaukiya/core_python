# Generator
# yield function

def disp(a, b):
    yield a
    yield b

result = disp(10, 20)

lst = list(result)

print(result)
print(type(result))

# print(lst)
# print(type(lst))

print("************************************************")
print()

def show(a ,b):
    while a<=b:
        yield a
        a+=1

result = show(1,5)

print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

for i in result:
    print(i)