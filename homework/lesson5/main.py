# HOMEWORK 1: Google time
import datetime
current_date_time=datetime.datetime.now()
print(current_date_time)
# HOMEWORK 2
# 1.Write a function that counts number of letters in a string you input
string=" Maliha"
count =0
for i in string:
    if i.isalpha():
        count=count+1
print(count)       
# 2.The function will have 1 parameter, the string that's letters you want to count.
def count_letters(user_input):
    count = 0
    for char in user_input:
        if char.isalpha():
            count = count+1
    return (count)
user_input=input("Enter a string:")
print(count_letters(user_input))

# HOMEWORK 3: Using results of function in another function
# Create a simple function with two parameters that returns their sum.
def add(x,y):
    result=x+y
    print(x,"+",y ,"=", result)

add(5,5) 
# Call the function and save the result into a variable (name of the variable is up to you
def add(x,y):
    result=x+y
    return(result)

print(add(5,5)) 
# Create another function with one parameter that decides if the parameter can be divided by 3
def division(x):
    result=x/3
    print(result)

division(6)
# Call the second function and use the variable that you created in the b) part as argument
def division(x):
    result=x/3
    return(result)

print(division(6))
# (Bonus) HOMEWORK 4: Rock, Paper, Scissors
import random
def play_game(user_choice):
    options=["Rock","Paper","Scissors"]
    computer_choice=random.randint(0,2)
    print("You choose {options[user_choice]}")
    print("Computer choose {options([computer_choice])}")
    if user_choice == computer_choice:
        return "Tie"  
    elif (user_choice==0 and computer_choice==0) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1):
         return "You win"
        
    else:
         return "You loose"
print(play_game(0))
print(play_game(1))
print(play_game(2))





