#Write a program that takes two numbers as input and displays their sum,difference, product and quotient

#Write a program that compares two integers and prints whether the first numbr is greater than, less than or equal to the second number

#Write a program that checks if a given number is between 10 and 20(20 is inclusive) using logical operators.
#Write a program that prints the squares of all integers from 1-10 using a for loop.
#Write a simple program that asks a user for their age; <=18, "Adult, you are qualified", 
#1. We have the following students details and marks.


























num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


sum = num1 + num2
difference = num1 - num2
product = num1 * num2


if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "undefined (cannot divide by zero)"


print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")

