
#Find the Prime Numbers in a Given Interval in Python


low,High=map(int,input().split())
primelist=[]
for i in range (low,High+1):
      flag=False
      if i<2:
            continue
      if i ==2:
            primelist.append(2)
            continue
      for x in range(2,i):
            if (i%x==0):
                  flag=1
                  break
            else :
                  flag=0
      if flag==0:
            primelist.append(i)
print(primelist)