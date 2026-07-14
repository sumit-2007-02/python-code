# get number from user and sum of two number
a = input("enter any number 1:-")
b = input("enter any number 2:-")
add = int(a) + int(b)
print("addition of two number is:-",add)

# find area of circle 
r = float(input("Enter Radius:-"))
ans = 3.14*r*r
print ("Area of circle = ",ans)

# perform arithmetic operation using format mentod
x = int(input("Enter any number 1 =")) 
y = int(input("Enter any number 2 ="))

print ("The sum of {0} and {1} is {2}".format(x,y,(x+y)))
print ("The sub of {0} and {1} is {2}".format(x,y,(x-y)))
print ("The mul of {0} and {1} is {2}".format(x,y,(x*y)))
print ("The div of {0} and {1} is {2}".format(x,y,(x/y)))
