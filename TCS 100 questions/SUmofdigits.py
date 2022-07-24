#Find the sum of the Digits of a Number
a =list(input())
sum=0
for i in range(len(a)):
      sum=sum+int(a[i])
print(sum)