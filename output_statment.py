print("the print() statement")
print("hello")
print()
print(3*"welcome")
print("city name is "+"amreli")
print("city name is ","amreli")

print("print (variable list) statement")
a,b = 2,4
print(a)
print(b)
print(a,b,sep=",")
print("hello\t\t\t wwelcome")

print("print(object) statement")
a = 5
print (a,"is input value")
print ("input is",a,"value")

print ("the print(formatting string) statement")
a = 10 
b = 20
print ("value is = %i" %a)
print ("value is = %d" %b)
s = "kscpsc"
print ("string = %s" %s)
t = "vab"
print ("%20s" %s)
print ("%20s" %t)
# print ("a = %d b = %d" (a,b) )
print ("%c %c " %(s[0],s[1]))
a = 123.4567
b = 12.45
print ("value is = %f" %a)
print ("%10.2f" %b)

n1,n2,n3 = 1,2,3
print ("number 1={0}, number 2={1}, number 3={2}".format(n1,n2,n3))
print ("number 1={1}, number 2={0}, number 3={2}".format(n1,n2,n3))

name, salary = 'ravi',12500.75
print ("hello {0}, your salary is {1}".format(name,salary))
# print ("hello {n}, your salary is {s}".format(name,salary))
print ("hello {:s}, your salary is {:2f}".format(name,salary))