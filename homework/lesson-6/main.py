# Excercise 1
# A- What is the name of a built-in function in "random" package which can generates random integers? 
 Answer: random.randint(a,b)
import random
random_number=random.randint(11,20)
print(random_number)
# B- Programming:
#    Using the function in section A, generate 10 integers that are between 1 and 100.
# import random
# random_numbers=[random.randint(1,100) for _ in range(10)]
# print(random_numbers)
#    Create a list. Call it rand_numbers. Use this list to save the generated integers. Print the list.
import random
rand_numbers=[random.randint(1,100) for _ in range(10)]
print(rand_numbers)
#    Calculate the average of the numbers in rand_numbers and display the result. (Feel free to write a function for this calculation.)
import random
rand_numbers=[random.randint(1,100) for _ in range(10)]
x=sum(rand_numbers) / len(rand_numbers)
print(x)
# C- Is there any built-in function in Python that can calculate average of numbers?
#    If "yes" use that function to calculate the average of rand_numbers and display the result.
import random
rand_numbers=[random.randint(1,100) for _ in range(10)]
import statistics
x=statistics.mean(rand_numbers)
print(x)
# D- Is the result of section B and C the same?
# the results are same.
Excercise-2
Create a Calculator that can perform four basic operations: addition, subtraction, multiplication, and division!
Your program asks the user to input the operation they want to perform and input two numbers.
Then it performs the operation and display the result.

# Instructions:
# Write a function for each arithmetic operation (add, subtract, multiply, divide).
# If the user entered an invalid operation, print an appropriate message to inform them.
# Your program handles errors (like dividing by zero) and invalid input (like entering a letter instead of a number).
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
       return"Error"
    return a/b
def calculator():
    print("Welcome to Basic Calculations!")
    print(" Available operations: add, substract, multiply, divide")
    operation= input("Enter the operation you want to perform:  ").strip().lower()
    if operation not in [ add, substract, multiply,divide]:
        print("Invalid operation, please choose from add, substract, multiply, divide")
        return 
    try:
        munber_1=float(input("Enter the first number:  "))
        number_2=float(input("Enter the second number:  "))
    except:
        print("invalid value, please enter a numerical value") 
        return  
    if operation == 'add':
        result = add(a, b )
    elif operation == 'subtract':
           result = substract(a,b)
    elif operation == 'multiply':
          result = multiply(a,b)
    elif operation == 'divide':
          result = divide(a,b) 
    print(f"The result is: {result}")  
calculator()       
# Exercise 3 
# Create "Guess the Number" game!
# Your program generates a random number between 1 and 100. Then asks the user to guess the random number.
# The user have 5 times to guess the number. If they cannot guess it correctly during this 5 rounds, they loose.
# Each round that the user guess the number wrong, your program gives the user a hint like "Too low!" or "Too high!".
# If the guess is correct it should print "Correct!" and prints the number of tries.

# Instructions:
# Write a function to generate a random number.
# Write a function to ask the user for their guess.
# Write a function to check if the guess is correct, too high, or too low.
# Write a main function that loops until the user guesses correctly and provides feedback.
import random
def generate_random_number():
    return random.randint(1,100)
def ask_for_guess():
    while True:
        try:  
            guess=int(input("Enter your guess between 1 and 100:"))
            if 1<=guess<=100:
                return guess
            else:
                print("Enter a number between 1 to 100")
        except ValueError:
            print("Invalid Error. Please enter an integer")
def check_guess(guess, number):
    if guess<1:
          return "too low"
    elif guess>100:
        return "too high"
    else:
        return "correct"
def play_game():
    number=generate_random_number()
    attempts=0
    max_attempts=5
    print("welcome to guess the number")
    print("you have 5 attempts to choose a number between 1 to 100")
    while attempts<max_attempts:
        guess=ask_for_guess()
        attempts=attempts+1
        result=check_guess(guess,number)
        if result=="correct":
            print(f"correct, you guess the number in {attempts} tries")
        else:
            print(result)
            remaining_attempts=max_attempts-attempts
            if remaining_attempts>0:
                print(f"You have {remaining_attempts} left")
            else:
                print(f"sorry you have used all your attempts, the current number was{number}")
play_game()





