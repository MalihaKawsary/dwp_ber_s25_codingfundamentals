# Exercise 1: Student Grouping
# import random
# students = [
#     {
#         "name": "Jane",
#         "choice": "Project B"
#     },
#     {
#         "name": "Janet",
#         "choice": "Project A"
#     },
#     {
#         "name": "Jack",
#         "choice": "Project A"
#     },
#     {
#         "name": "Jimmy",
#         "choice": "Project B"
#     },
#     {
#         "name": "Jean",
#         "choice": "Project A"
#     },
#     {
#         "name": "Juan",
#         "choice": "Project B"
#     },
#     {
#         "name": "Juanita",
#         "choice": "Project B"
#     },
#     {
#         "name": "Janine",
#         "choice": "Project A"
#     },
#     {
#         "name": "Jill",
#         "choice": "Project B"
#     },
#     {
#         "name": "John",
#         "choice": "Project B"
#     },
# ]

# def pick_random_name_project (students, project_choice):
#     filtered_students=[]
#     for s in students: 
#         if s["choice"]==project_choice:
#             filtered_students.append(s)

#     selected= random.sample(filtered_students,2)
#     # choice returns duplicate but sample returns no duplicate with random
#     return [(project_choice, s["name"]) for s in selected]


# print(pick_random_name_project (students, "Project A") )
# print(pick_random_name_project (students, "Project B") )
# Exercise 2: Meal cost calculator
import inquirer
import random

def inquire(name):
  breakfast_base = random.randint(2, 6)
  lunch_base = random.randint(10, 21)
  dinner_base = random.randint(30, 51)
  questions = [
      inquirer.List(
          "breakfast",
          message=f"How much did {name} pay for breakfast? 🥐 ☕",
          choices=[f"${breakfast_base}", f"${breakfast_base + 2}"],
      ),
      inquirer.List(
          "lunch",
          message=f"How much did {name} pay for lunch? 🍔",
          choices=[f"${lunch_base}", f"${lunch_base + 7}"],
      ),
        inquirer.List(
          "dinner",
          message=f"How much did {name} pay for dinner? 🍽️",
          choices=[f"${dinner_base}", f"${dinner_base + 15}"],
      ),
  ]
  
  transactions = inquirer.prompt(questions)
  return {name: transactions}

people = ["John", "Jane", "Janet"]
result = [inquire(person) for person in people]
print("Result: ")
pprint(result)

# Exercise 4: Meal cost game
# def play_game():
#     name = "ReDi"
#     lower_limit = 42 
#     higher_limit = 55 
#     meals = inquire(name)[name] 
#     total = 0

#     for meal_value in meals.values(): 
#         total += convert_dollars(meal_value) 
#     if (lower_limit > total or higher_limit < total): 
#         print("You lost.. try again!") 
#     else: 
#         print("Congrats! You won 👏")
# play_game()
sample_credit_card_number = '1234567890987654'
expected_credit_card_result = 'XXXXXXXXXXXX7654'

def mask_credit_card_number(credit_card_number):
    masked_credit_card_number = 'x'*(len(credit_card_number)-4)+credit_card_number[-4:]
    
    return masked_credit_card_number
print('Expected result: ', expected_credit_card_result)
result = mask_credit_card_number(sample_credit_card_number)
print('Your result:', result)