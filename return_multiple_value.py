# a function that returns multiple results
def sum_sub_mul_div(a,b):
  c=a+b
  d=a-b
  e=a*b
  f=a/b
  return c,d,e,f
#get resuts from sum_sub_mul_div() function and store into t
t=sum_sub_mul_div(10,5)
#display the results using for loop
print("The results are")
for i in t:
   print(i,end=", ")
