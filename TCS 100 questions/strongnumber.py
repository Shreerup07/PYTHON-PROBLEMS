#STRONG NUMBER
def factorial(num):
      if num==0 or num==1:
            return 1
      else:
            return (num*factorial(num-1))
n=input()
l=[]
temp=0

for i in range (len(n)):
      l.append(factorial(int(n[i])))
#print(l)
for z in range(len(l)):
      temp=temp+int(l[z])
#print(temp)
if temp==int(n):
      print("Strong Number")
else:
      print("not a strong number")

