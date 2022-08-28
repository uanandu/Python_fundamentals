#here we do fundamental exercises for python

#1. Write a program that asks the user for their name and then prints a greeting to the user.
# Write your code here
from functools import reduce


name = input("What is your name? ")
print("Hello " + name)

#2. Write a program that asks the user for a number n and gives the square of n.
# Write your code here
number = int(input("Give me a number: "))
print("Your number is: ", number)
print("Your square is: ", number ** 2)

#3. Write a program that asks the user for two numbers and then prints the sum of those two numbers.
# Write your code here
number = int(input("Give me a number: "))
number2 = int(input("Give me another number: "))
print("The sum of your numbers is: ", number + number2)

#4. Write a program that asks user for a range of numbers and then prints the sum of those numbers.
# Write your code here
number = int(input("Give me a number: "))
number2 = int(input("Give me another number: "))
reduced_number = reduce(lambda x, y: x + y, range(number, number2 + 1))
print("The sum of your numbers is: ", reduced_number)

#5. Write a program that asks the user for a number n and gives the sum of the numbers 1 to n.
# Write your code here
number = int(input("Give me a number: "))
reduced_number = reduce(lambda x, y: x + y, range(1, number + 1))
print("The sum of your numbers is: ", reduced_number)

#6. Write a program that asks the user for a range of numbers and then prints out if it is even or odd.
# Write your code here
number = int(input("Give me the starting range: "))
number2 = int(input("Give me the end range: "))
for i in range(number, number2 + 1):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
