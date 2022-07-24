#Perfect Number Code in Python
def perfect_number(num):
      l=[]
      temp=0
      for i in range(1,num):
            if(num%i==0):
                  l.append(i)
      print(l)
      for z in range(len(l)):
            temp=temp+int(l[z])
      print(temp)
      if temp==num:
            print("THE NUMBER IS A PERFECT NUMBER ")
      else:
            print("THE NUMBER IS NOT A PERFECT NUMBER ")
num=int(input())
perfect_number(num)
