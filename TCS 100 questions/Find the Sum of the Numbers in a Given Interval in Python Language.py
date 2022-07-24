#Find the Sum of the Numbers in a Given Interval in Python Language
def total_sum(num1,num2):
      sum=0
      for i in range(num1,num2+1):
            sum=sum+i
      print(sum)
#num1=int(input())
#num2=int(input())
num1,num2=map(int,input().split( ))

total_sum(num1,num2)