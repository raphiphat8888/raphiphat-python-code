"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random
#refactor != debug

random_number = random.randint(1, 20)
heart=6
print(" === SIMPLE GUESSING GAME ===")
print("Guess my number between 1 and 20!")
print("You have 6 attempts")
while True:
    number=int(input("what is number do you think ?"))
    if(number==random_number):
        print("good gay bro")
        break
    elif (number>random_number):
        heart=heart-1
        print("your number is more")
        print(f"You have {heart} attempts")
    elif (number<random_number):
        heart=heart-1
        print("your number is less")
        print(f"You have {heart} attempts")
    if(heart==0):
        print("you death")
        break

print("===number random===")
print(random_number)
    

