def add(farg,*args):   # *args can take 0 or more values
    """to add given numbers"""
    print("Formal arguments = ",farg)
    sum=0
    for i in args:
        sum+=i
    print("sum of all numbers= ",(farg+sum))

# call add() and pass arguments
add(5,10)
add(15,20,25,30)