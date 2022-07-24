#Find the Armstrong Numbers between Two Intervals using Python
def armstrong_numbers(low,high):
      for i in range(low,high+1):
            i=str(i)
            temp=0
            for z in range(len(i)):
                  temp=temp+int(i[z])**3
            if temp==int(i):
                  print(temp)
            




low=int(input())
high=int(input())
armstrong_numbers(low,high)
