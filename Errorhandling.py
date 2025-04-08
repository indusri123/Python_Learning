try :
    num = int(input("Enter a num : "))
    print(50/num)
except ZeroDivisionError :
    print("Cant divide by zero") 
except ValueError :
    print("That's not a number")                  