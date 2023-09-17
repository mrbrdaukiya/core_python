#Formatting String
#f- string (type- 3)

#Integer
print("******************** Integer *******************")

a = 10
b = 20
value = f"{a}"
print(value)
print(f"{a}")
print(f"{a}           {b}")
print(f"{b} {a}")


print()


#Float
print("******************** Float *******************")

c = 10.56
d = 20.42
print(f"{c}")
print(f"{c} {d}")
print(f"{d} {c}")


print()


#String
print("******************** String *******************")
f_name = "Guru"
l_name = "Choudhary"
print(f"{f_name}")
print(f"{f_name} {l_name}")
print(f"{l_name} {f_name}")



print()


#String and Integer
print("******************** Integer and String *******************")
name = "Guru"
age = 10
print(f"Hello My Nmae is {name} and My age is {age} year.")
print(f"{name} {age}")
print(f"{age} {name}")




print()


#Integer
print("******************** Integer *******************")
num = 15
print(f"{num}")
print(f"{num:d}")
print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")
print(f"{num:*<5d}")
print(f"{num:*>5d}")
print(f"{num:^5d}")
print(f"{num:*^5d}")


print()


#Float
print("******************** Float *******************")
num = 15.65
price = 16.65123456789
print(f"{num}")
print(f"{num:f}")
print(f"{num:8f}")
print(f"{price:.20f}")
print(f"{num:8.3f}")
print(f"{num:+8.2f}")
print(f"{num:<8.2f}")
print(f"{num:*<8.2f}")
print(f"{num:*>8.2f}")
print(f"{num:^8.2f}")
print(f"{num:*^8.2f}")


print()


#String
print("******************** String *******************")
name = "Guru"
print(f"{name}")
print(f"{name:s}")
print(f"{name:8s}")
print(f"{name:<8}")
print(f"{name:*<8}")
print(f"{name:>8}")
print(f"{name:*>8}")
print(f"{name:^8}")
print(f"{name:*^8}")


print()


#String
print("******************** String *******************")
name = "GuruChoudhary"
print(f"{name}")
print(f"{name:.3s}")
print(f"{name:8.3s}")
print(f"{name:<8.3s}")
print(f"{name:*<8.3s}")
print(f"{name:>8.3s}")
print(f"{name:*>8.3s}")
print(f"{name:^8.3s}")
print(f"{name:*^8.3s}")

print()

price = 1234567890
print(f"{price:,}")
print(f"{price:_}")

name = "Rahul"
age = 25
print(f"My Name is {name} and age is {age}")

print(f"{10*8}")

a = 50
b = 3
print(f"{a/b:.2%}")

print()

value = (10, 20)
print(f"{value[0]} {value[1]}")

print()

data = {'rahul':2000, 'sonam': 3000}
print(f"{data['rahul']:d} {data['sonam']:d}")

print()

name = "GuruChoudhary"
print(f"{name.upper()}")

print(f"{{10}}")

print()

#Date and Time
print("************ Date and Time ************")
from datetime import datetime
today = datetime(2023, 8, 20)
print(f"{today}")
print(f"{today:%d/%b./%Y- %A}")