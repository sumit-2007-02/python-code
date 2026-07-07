name = ["vupul", "rakesh", "dinesh", "dhamo"]
for n in name:
    print(n)
postal = {'delhi': 110001, 'chennai': 600001, 'amreli': 365601}
for city in postal:
    print(city, postal[city], end=" ")

x = 30
l = [10, 20, 30, 40, 50]
if (x in l):
    print("x is present")
else:
    print("x is not present")

x = 10 
l = [10, 20, 30, 40, 50]
if (x not in l):
    print("x is not present")
else:
    print("x is present")