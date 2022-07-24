
#Check Whether a Given Number is an Armstrong Number or Not
def check_armstrong(a):
      temp=0
      for i in range(len(a)):
            temp=temp+int(a[i])**3
      print(temp)
      if temp==int(a):
            print("YES ARMSTRONG")
      else:
            print("NOT ARMSTRONG")

      



a=input()
check_armstrong(a)