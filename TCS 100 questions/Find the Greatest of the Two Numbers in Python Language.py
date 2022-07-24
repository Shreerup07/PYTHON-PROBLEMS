#Find the Greatest of the Two Numbers in Python Language
def greatest_number(x,y):
     
      if x==y:
            print("Numbers are equal")
      elif x>y:
            print(x)
      else:
            print(y)




x,y=map(int,input().split())
greatest_number(x,y)