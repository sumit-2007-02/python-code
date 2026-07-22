#local variable in a function
def myfunction():
    a=1 #this is local var
    a+=1
    print("local variable=",a)
myfunction()
# print(a) #error, not available

#global variable in a function
a=1 #this is global var
def myfunction():
   b=2 #this is local var
   print("a = ",a) #display global var
   print("b = ",b) #display local var
myfunction()
print("global variable= ",a) #available
# print(b) #error,not available