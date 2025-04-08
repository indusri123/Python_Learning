#Write a number guessing game using while loop
import random

def number_guessing_game() :
    number_to_guess = random.randint(1,100)
    attempts = 0
    print("\n")
    print("         Hello, Welcome to Number Guessing Game!")
    print("         I'm guessing a number between 1 to 100")
    print("         Can u guess it?\n")
    
    while True :
        try :
            guess = int(input("Enter your guess : "))
            if guess > number_to_guess :
                print("Too High!, Try Again. \n")
                attempts +=1
            elif guess < number_to_guess :
                print("Too Low!, Try Again. \n")
                attempts +=1
            else :
                print(f"Correct! you have guessed in {attempts} attempts.")
                break 
        except ValueError :
            print("Thats not a number.") 

number_guessing_game()                      
