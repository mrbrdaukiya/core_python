from numpy import *
a = array([100, 12, 300, 400, 500])
b = array([101, 20, 30, 401, 50])
result = where(a>b, a, b)
print(result)