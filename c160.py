# Higher Ordar Function
# Reduce Function
from functools import * #(can use reduce here also)
a = [10, 20, 30, 40, 50]


result = reduce(lambda n,m : n+m,a)

print(result)

print(type(result))