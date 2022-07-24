#PROGRAM TO FIND FACTOR OF A NUMBER 
def factors(num):
      if num==0 :
            print(" a number greater than 0 ")
      else :
            for i in range(2,num+1):
                  if (num%i==0):
                        print(i,end=" ")
num=int(input())
factors(num)