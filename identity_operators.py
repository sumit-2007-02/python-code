a = 10 
b = 10
print(id(a))
print(id(b))
if (a is b):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
if (a is b):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")