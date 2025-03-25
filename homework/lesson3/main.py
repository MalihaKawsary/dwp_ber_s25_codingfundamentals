# Basic Arithmetic operations
first_number=10
second_number=5
addition=first_number+second_number
print(addition)
substraction= first_number-second_number
print(substraction)
multiplication=first_number*second_number
print(multiplication)
division=first_number/second_number
print(division)
# BONUS
my_number_1=input("What is my first number")
my_number_2=input("What is my second number")
convert_1=int(my_number_1)
convert_2=int(my_number_2)
add=convert_1+convert_2
print("Result",add)
# Modulus and Exponentiation
number=7
print(number%3)
print(7**2)
# BONUS
x=input("What is my number")
convert=int(x)
modulus=convert%3
print(modulus)
# odd or even
number=4
if number%2==0:
    print("4 is even")
else:
    print("4 is odd")
# BONUS
x=input("What is my number")
convert=int(x)
if convert%2==0:
    print("my number is even")
else:
    print("my number is odd")
# compare two numbers
number_1=10
number_2=5
print(number_1>number_2)
num_1=10
num_2=20
print(num_2>num_1)
n_1=10
n_2=10
print(n_1==n_2)
# BONUS
x=input("what is your first number")
y=input("what is your second number")
convert_1=int(x)
convert_2=int(y)
if convert_1>convert_2:
        print("convert_1 is greater than convet_2")
elif convert_1==convert_2:
      print("convert_1 is eqeal to  convert_2")
else:
       print("convert_1 is less than convert_2")
# Print numbers 1 to 10
for count in range(1,11):
    print(count)
# Multiplication Table
x=input("What is the number")
convert=int(x)
for i in range(1,11):
    print(convert,"*",i,"=",convert*i)
# Bonus Questions
# FizzBuzz
for i in range(1,21):
  if i%3==0:
    print("Fizz")  
  elif i%5==0:
    print("Buzz")
  elif i%15==0:
    print("FizzBuzz")
  else:
    print(i)
# Leap Year
x= input("what is the year")
conversion=int(x)
if conversion % 400 == 0:
  print("The Year is leap Year")
elif (conversion % 4 == 0 and conversion % 100 != 0):
    print("The Year is leap Year")
elif (conversion % 100 == 0 and conversion % 400 != 0):
         print(" The Year is not leap year")
else:
     print(" The Year is not leap year")

