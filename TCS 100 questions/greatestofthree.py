#greatest OF the tree numbers
#syntax 1:
def greatest_of_three(x,y,z):
      if(x>y and x>z):
            print(x)
      elif(y>x and y>z):
            print(y)
      
      else:
            print(z)
x,y,z=map(int,input().split())
greatest_of_three(x,y,z)
