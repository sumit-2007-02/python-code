tup = ()
print (tup)

#uaing string
tup = ('Geeks', 'For')
print (tup)

# using list
li = [1, 2, 3, 4, 5, 6]
print (tuple(li))

# using built-in function
tup = tuple('Geeks')
print (tup) 

t = (10, 'kscpsc', 10.20)
for i in t:
    print (i,end = " ")

tup = tuple('Geeks')
print (tup[0])
print (tup[1:4])
print (tup[:3])

# tuple unpacking
tup = ("Geeks", "For", "Geeks")

# this line unpacks the values of tuple1
a, b, c = tup
print(a)
print(b)
print(c)

tup = tuple("kamanisciencecollage")
print(tup[0])
print(tup[1:12:2])
print(tup[0:10:3])
print(tup[3:1])
print(tup[1:15:6])
print(tup[10:0:-1])
print(tup[10:0:-2])

tup1 = (0, 1, 2, 3)
tup2 = ("Geeks", "For", "Geeks")
tup3 = tup1 + tup2
print(tup3)

tup = (0, 1, 2, 3, 4)
del tup
# print(tup)