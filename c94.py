#Formatting String
#type - 1 ( C-style string Formatting)[old style]
print("%d" % 432)
print("%d %d" % (432, 535))
print("%f" % 432.123)
print("%f %f" % (432.123, 10.3))
print("%f" % 432.123456)
print("%f" % 432.12345651)
print("%s" % "guru")
print("%s %s" % ("Hello", "guru"))
print("%d %s" % (432, "guru"))

print()

a = "%d" % 432
print(a)
print(type(a))

print()

print("%(nm)s %(ag)d" % {'ag': 432, 'nm':"guru"})

print()

print("%d" % 432)
print("%                      d                   hello" % 432)
print("%+d" % 432)
print("%8d" % 432)
print("%08d" % 432)
print("%f" % 432.123)
print("%.3f" % 432.123)
print("%.2f" % 432.123)
print("%.2f" % 432.128)
print("%9.2f" % 432.128)
print("%09.2f" % 432.128)
print("%09.2f" % 458624432.124)

print()
print("My Age is %d and I'm from Mahadev Nagar." % 25)
b = "My Age is %d and I'm from Mahadev Nagar." % 25
print(b)



