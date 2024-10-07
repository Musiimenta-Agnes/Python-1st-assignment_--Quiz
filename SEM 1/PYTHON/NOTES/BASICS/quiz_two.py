#1. Write a program that takes two numbers  as  inputs and dispays thier sum their difference, thier  product and thier quotient.
#2. Write a program that compares two integers and prints whether the first number is greater than, less than  or equaal to the second number.
 #3. Write a program that checks if a given number is between 10 and 20 (20 is inclusive using logical operators.) 
#4. Write a program that prints the squeres of all integres from 1 to 10 using a for loop.


              #ANSWERS
# NO.1
first_number = int(input('Enter first number: '))
second_number = int(input('Enter scond number: '))
#when dealing with input function in operations, we always cast inorder to change to integers or float.
# This  is because input function operats with strings, so we cast in the 'int' inorder to allow the arthmatic operations. 



sum = (first_number + second_number)
print(f"The sum of  {first_number} and {second_number} is {sum}")

difference = (first_number - second_number)
print(f"The differnce of  {first_number} and  {second_number} is  the {difference}")


product = first_number * second_number
print(f"The product of  {first_number} and  {second_number} is {product}")

quotient = (first_number / second_number)
print(f"The quotient of  {first_number} and {second_number} is {quotient}")

modulous = first_number % second_number
print(f"the modulous of {first_number} and  {second_number} is {modulous}") 

floor_division = first_number // second_number
print(f"The floor division of {first_number} and {second_number} is {floor_division}")



#NO.2 
# Comparisons are used to compare (The use of if loops and we expect "true" and "false")

number_one = 10
number_two = 2

if number_one > second_number:
    print(f"{number_one} is greater than {number_two}")
elif number_one < number_two:
    print(f"{number_one} is less than {number_two}")
else:
    print(f"They are equal")





