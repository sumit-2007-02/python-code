s = "ABCDEF"
print (s[0])
print (s[4])

print (s[-3])
print (s[-5])

print (s[1:4])
print (s[:3])
print (s[3:])
print (s[::-1])

for char in s:
    print (char)

s = "aBCDEF"
s = "A" + s[1:]
print(s)

s = "ABC"
del s 

s= "ABCDEF"
s1 = "h" + s[1:]
s2 = s.replace ( "ABC" , "abc" )
print(s1)
print(s2)

s = "kscpsc"
print (len(s) )

s = "Hello World"
print(s.upper())
print(s.lower())

s = "   ABC   "
print (s.strip())

s = "python is fun"
print (s.replace ("fun","awesome"))

s1 = "Hello"
s2 = "World"
print (s1 + " " +s2)

s = "Hello "
print (s * 3)