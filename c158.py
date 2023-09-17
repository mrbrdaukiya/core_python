# Higher Ordar Function
# Filtter Function

a = [10, 50, 60, 80, 90, 5, 45, 65]

# def high_marks(n):
#     if n >=60:
#         return True

# result = list(filter(high_marks, a))

result = list(filter(lambda n: (n>=60), a))

# result = list(filter(None, a))
print(result)

print(type(result))

for i in result:
    print(i)

