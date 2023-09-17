#numpy

# import numpy
# stu_roll = numpy.array([101, 102, 103, 104,105])
# stu_roll = numpy.array([101, 102, 103, 104,105], dtype=float)
# stu_roll = numpy.array([101, 102, 103, 104,10.5])
# stu_roll = numpy.array(["a", "b","c", "d","e"])
# stu_roll = numpy.array(["ashok", "hari","bhomaram", "guru","manish"])
# print(stu_roll)
# print(stu_roll.dtype)
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])

# from numpy import *
# stu_roll = array([101, 102, 103, 104,105])
# print(stu_roll)
# print(stu_roll.dtype)
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])

#modify array
from numpy import *
stu_roll = array([101, 102, 103, 104,105])
print(stu_roll)
print(stu_roll.dtype)

stu_roll[1] = 110

print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])