#Find the Sum of the First N Natural Numbers in Python

def total_sum(num):
      sum=0
      for i in range(num+1):
            sum=sum+i
      print(sum)
num=int(input())
total_sum(num)