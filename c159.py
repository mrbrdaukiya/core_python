# Higher Ordar Function
# map Function

a = [10, 20, 30, 40, 50]
# b = [1, 2, 3, 4, 5]

# def inc(n):
#     return n+2

# result = list(map(inc, a))

result = list(map(lambda n : n+2, a))

# result = list(map(lambda n, m: n + m, a,b))


print(result)
print(type(result))
for i in result:
    print(i)