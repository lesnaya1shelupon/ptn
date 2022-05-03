import math
print("Write 2 sides the legs of the triangle ")
a = int(input("1 side: "))
b = int(input("2 side: "))
c = (a**2) + (b**2)
d = math.sqrt(c)
print("hypotenuse of a triangle = {}".format(d))