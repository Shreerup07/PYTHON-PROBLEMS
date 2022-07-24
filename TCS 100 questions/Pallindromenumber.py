#Check Whether or Not the Number is a Palindrome in Python Language
def pallindromenumber(num):
      num_new=str(num)
      num_new1=num_new[::-1]
      if num_new==num_new1:
            print("PALLINDRIME")
      else:
            print("NOT PALLINDROME")
      
            
num=int(input())
pallindromenumber(num)
