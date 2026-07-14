# py sum_using_cmd.py 100 200
import sys
ans = int (sys.argv[1]) + int(sys.argv[2])
print ("sum is = ",ans)
print ("program name is = ",sys.argv[0])
n = len(sys.argv)
print ("Total Arguments = ",n)
args = sys.argv
print ("Arguments are = ",args)
for i in args :
    print (i)
