# Anonymous Function or Lambdas Function
sum = lambda x :print(x)
sum(20)



print()
print("*************************")
print()

show = lambda x, y :print( x + y)
show(10,20)


print()
print("*************************")
print()

show = lambda x, y : (x + y, y - x)
a, s = show(10,20)
print(a)
print(s)



print()
print("*************************")
print()

show = lambda x, y =20 : x + y + 20
print(show(20))