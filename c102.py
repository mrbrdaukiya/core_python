#String Function
name = "Guru Choudhary"
# old = "Guru"
# new = "Ashok"
result =  name.replace("Guru", "Ashok")
print("Old result : ", name)
print("New result : ",result)

print()

name = "Hello-How-are-you"
result =  name.split('-')
print("Old result : ", name)
print("New result : ",result)

name = "Guru Choudhary"
result =  name.split(' ')
print("Old result : ", name)
print("New result : ",result)

print()

name = ('Hello', 'How', 'are', 'you')
result =  '_'.join(name)
print("Old result : ", name)
print("New result : ",result)

print()

name = ('Hello', 'How', 'are', 'you')
result =  ' '.join(name)
print("Old result : ", name)
print("New result : ",result)