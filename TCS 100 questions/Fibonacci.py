#PRINT THE FIBONACCI OF THE GIVEN NUMBER:
def fibonacci(i):
      if i<=1:
            return i
      else:
            return (fibonacci(i-1)+fibonacci(i-2))
num=int(input())
if num<=0:
      print("A positive number")
for i in range(num):
      print(fibonacci(i),end=" ")