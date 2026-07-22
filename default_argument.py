#default arguments demo
def grocery(item,price=88.00):
 """to display the given arguments"""
 print("item=%s"%item)
 print("price=%.2f"%price)
#call grocery() and pass 2 arguments
grocery(item="sugar",price=48.50) #keyword arguments
grocery(item="Oil") #keyword arguments