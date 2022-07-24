# Check Whether a Number is a Prime or Not
def prime_number(x):
    flag = False
    if x > 0:

        if x == 1:
            flag = True

        elif x > 1:

            for i in range(2, x):
                if(x % i == 0):
                    flag = True
                    break
        if flag == True:
            print("NOT A PRIME")
        else:
            print("A PRIME NUMBER")


x = int(input())
prime_number(x)
