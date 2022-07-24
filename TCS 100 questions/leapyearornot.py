def leapyear(x):
      if (x%400==0)or(x%4==0 and x%100!=0):
            print(f"The year {x} is a leapyear")
      else :
            print(f"The year {x} is not a leapyear")
x= int(input())
leapyear(x)