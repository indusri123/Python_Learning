#Write a function to calculate the factorial of a number
#Handle the error when user inputs non-numeric value

try :
    num = int(input("Enter a number : "))
    fact = 1
    if num <0 :
        print("Cant find factorial for negative numbers")
    else :    
        for i in range(2,num+1) :
            fact = fact * i
        print(fact)
except ValueError :
    print("Thats not a number")        