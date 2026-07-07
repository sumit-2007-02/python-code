a = {10, 10, 10, 10, 20, 30, 40}
print(a)    
for i in a:
    print(i,end = " ")
ch = set("hello")
print(ch)

a.update([50,60])
a.remove(20)
for i in a:
    print(i,end = " ")
