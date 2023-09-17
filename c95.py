#Formatting String
#Format() Method(type- 2)
# Ex - print("Replacement Field".format(values))
# RF = {index/key: [fill][align][sign][#][0][width][,][.precision]type}
print("******************** Integar ****************")
print("{}".format(10))               # Do not Write Space btween{}
print("{} {}".format(10, 20))
print("{0}".format(10))
print("{0} {1}".format(10, 20))
print("{1} {0}".format(10, 20))
print("{num1}".format(num1 = 10))
print("{num1} {num2}".format(num1 = 10, num2 = 20))
print("{num2} {num1}".format(num1 = 10, num2 = 20))


print()


print("******************** Float ****************")
print("{}".format(10.56))               # Do not Write Space btween{}
print("{} {}".format(10.56, 20.42))
print("{0}".format(10.56))
print("{0} {1}".format(10.56, 20.42))
print("{1} {0}".format(10.56, 20.42))
print("{num1}".format(num1 = 10.56))
print("{num1} {num2}".format(num1 = 10.56, num2 = 20.42))
print("{num2} {num1}".format(num1 = 10.56, num2 = 20.42))


print()


print("******************** String ****************")
print("{}".format("Guru"))               # Do not Write Space btween{}
print("{} {}".format("Guru", "Choudhary"))
print("{0}".format("Guru"))
print("{0} {1}".format("Guru", "Choudhary"))
print("{1} {0}".format("Guru", "Choudhary"))
print("{str1}".format(str1 = "Guru"))
print("{str1} {str2}".format(str1 = "Guru", str2 = "Choudhary"))
print("{str2} {str1}".format(str1 = "Guru", str2 = "Choudhary"))


print()


print("******************** Integar With String ****************")
print("My Name is: {}".format("Guru"))
print("{} {}".format(10, "Choudhary"))
print("{0} {1}".format(10, "Choudhary"))
print("{1} {0}".format(10, "Choudhary"))
print("{str1}".format(str1 = "Guru"))
print("{num1} {str1}".format(num1 = 10, str1 = "Choudhary"))
print("{str1} {num1}".format(num1 = 10, str1 = "Choudhary"))

print()

print("******************** Integar ****************")
print("{}".format(15))
print("{:d}".format(15))
print("{0:d}".format(15))
print("{num:d}".format(num = 15))  

print()

#Integer
print("{num:d}".format(num = 15))
print("{num:5d}".format(num = 15))
print("{num:05d}".format(num = 15))
print("{num:+5d}".format(num = 15))
print("{num:<5d}".format(num = 15))
print("{num:*<5d}".format(num = 15))
print("{num:*>5d}".format(num = 15))
print("{num:^5d}".format(num = 15))
print("{num:*^5d}".format(num = 15))
print("{num:*^6d}".format(num = 15))


print()

print("******************** Float ****************")
print("{}".format(15.65))
print("{:f}".format(15.65))
print("{0:f}".format(15.65))
print("{num:f}".format(num = 15.65)) 

print()

#Float
print("{num:f}".format(num = 15.65))
print("{num:8f}".format(num = 15.65))
print("{num:8.3f}".format(num = 15.65))
print("{num:+8.2f}".format(num = 15.65))
print("{num:<8.2f}".format(num = 15.65))
print("{num:*<8.2f}".format(num = 15.65))
print("{num:*>8.2f}".format(num = 15.65))
print("{num:^8.2f}".format(num = 15.65))
print("{num:*^8.2f}".format(num = 15.65))
print("{num:*^9.2f}".format(num = 15.65))

print()

#String
print("******************** String ****************")
print("{:8s}".format("guru"))
print("{:<8}".format("guru"))
print("{:*<8s}".format("guru"))
print("{:>8}".format("guru"))
print("{:*>8s}".format("guru"))
print("{:^8s}".format("guru"))
print("{:*^8s}".format("guru"))

print()

print("******************** Truncating String ****************")
print("{:.3s}".format("GuruChoudhary"))
print("{:8.3s}".format("GuruChoudhary"))
print("{:<8.3}".format("GuruChoudhary"))
print("{:*<8.3}".format("GuruChoudhary"))
print("{:>8.3}".format("GuruChoudhary"))
print("{:*>8.3s}".format("GuruChoudhary"))
print("{:^8.3s}".format("GuruChoudhary"))
print("{:*^8.3s}".format("GuruChoudhary"))

print()

print("{:,}".format(1234567890))
print("{:_}".format(1234567890))
name = "Guru"
age = 62
print("My Name is {} and age is {}".format(name , age))

value = (10, 20)
print("{0[0]} {0[1]}".format(value))

data = {'rahul': 2000, 'sonam': 3000}
print("{0[rahul]:d} {0[sonam]:d}".format(data))
print("{d[rahul]:d} {d[sonam]:d}".format(d = data))
print("{rahul} {sonam}".format(**data))