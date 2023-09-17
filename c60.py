#numpy For Loop

# from numpy import *
# stu_roll = array([101, 102, 103, 104,105])
# for i in stu_roll:
#     print(i)

# from numpy import *
# stu_roll = array([101, 102, 103])
# n = len(stu_roll)
# for i in range(n):
#     print("index", i, "=" , stu_roll[i])

#modifition
from numpy import *
stu_roll = array([101, 102, 103])
stu_roll[1] = 110
n = len(stu_roll)
for i in range(n):
    print("index", i, "=" , stu_roll[i])