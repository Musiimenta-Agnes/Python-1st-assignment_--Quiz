#ASSIGNMENT

#1. Write a program that checks if a given number is between 10 and 20 (20 is inclusive using logical operators.) 


number = int(input("Enter number: "))
if 10 < number <= 20:
    print("number is between 10 and 20")
else:
    print("number is not between 10 and 20") 




#2. Write a program that prints the squeres of all integres from 1 to 10 using a for loop.


intergers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in intergers:
    x = x*x
    print(x)

# 3. Write a simple program that asks a user for thier age if the user is greater or equal to 18, 
# print you are an adult and you are qualified.
#else you are not qualified.



age = int(input("Enter your age: "))
qualified_adult = 18
if age >= qualified_adult: 
    print(f"You are an adult and you are qualified")
else:
    print(f"You are not qualified")




#4.  We have the following studentsdetails and marks, entr these details from the keyboard.(Here we use the input function, wen
#told to interract with the keyboard )
#STudent name = Ritah Liz
# Studentnumber = SEP23/BCS/14
#Programming = 78
#Data science = 89
#Computer Application = 55
#Calculate the average mark and print the answer in 3 decimal places.

student_name = input("Enter your name: ")
student_number = input("Enter the student number: ")
programming = int(input("Enter the programming mark: "))
data_science = int(input("Enter the  data science mark: "))
computer_application = int(input("Enter the computer application mark: "))

total_mark = programming + data_science + computer_application
number_of_course_units = 3
average_mark = total_mark / number_of_course_units
print(f"The average mark is: {average_mark:.3f}") #should be 3 decimal places



#5. Write aprogram that converts celicious temperature to faranahight, the program shouold ask the user to enter the
#temperature in celicious and then display the temperature converted to faranahight degrees.    `   DZXC VBN. WSCVB`

celsius = int(input("Enter th temperature in celicious degrees: "))
farahnaheight=(celsius * 1.8)
print(f"{celsius} degree celsius is equal to: {farahnaheight} degree faranaheight")



#6. A cars miles per gulton can be calculated with  the following formular:MPG = Miles Driven/ Gulton of gas used.
# Write a program that asks the user for the number of miles driven and gultons used. 
# It should calculate the cars miles driven per gulton and display the result 
#using this formular: MPG = Miles Driven/ Gulton of gas used
   
   
   
miles_driven = int(input("Enter the number of miles: "))
gultons_used = int(input("Enter the number fo gultons used: "))
mpg = miles_driven / gultons_used 
print(f"The car's mies driven per gulton is: {mpg} ")