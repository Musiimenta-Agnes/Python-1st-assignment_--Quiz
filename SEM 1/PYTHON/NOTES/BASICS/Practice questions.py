#1. The voleum of a sphere with radius r is (4/3)* pie r**2.
# What is the volume of a asphere with radius 5
#Make sure the prigaram enters the radius from the keyboardand provide the answer in 2 decimal places.

r = int(input("Enter radius: "))
volume = 4/3*22/7*r**2
print(f"The volume of a sphere whose radius is 5 is {volume:.2f}")



#2. Create a program to calculate the area of a triangle (1/2* base*height).
#Base and hehght should be enterd using the keyboard.

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 1/2*base*height
print(f"The area of a triangle is {area}")


#3. WITI has tasked you to automate a simple grading system,
#As a python student, write a program used to display the grades that
#the students wil be receiving based on the mark scored in a subject.
#The gardes are:
# 90% -100%  Grade is A
# 80% - 89%  Grade is B
# 70 - 79%   Grade is C
# 60% -69%  Grade is D
# 50% - 59%  Grade is E
# 50% - Fail

def calculate_grades():
 
 print("Calculating the student's grades")
 mark = int(input("Enter the mark: "))

 if 90<=mark<=100:
        print(f"Grade A")
 elif 80<= mark<=89:
        print(f"Grade B")
 elif 70<=mark<=79:
        print(f"Grade C")
 elif 60<=mark<=69:
        print("Grade D")
 elif 50<= mark<=59:
        print(f"Grade E")
 else:
        print(f"Fail")

        calculate_grades()


#4. WITI academy is proposing a sacco to help students save their money.
# Design a platform that will do the following.
# Welcome to, WITI sacco.
# 1. Deposit Money
# 2. Withdraw Money
# 3. Check Balance
# Ensure that if the students selects 1, money is depositedand the minimum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdraw is 500.
# If the sudebnts selects 3, the account balance should be displayed.

def Sacco_transaction():
      account_balance = 0
      run = 1
      while run == 1:
            

            print('Welcome to WITU Guild Sacco')
            print('1. Deposite')
            print('2. Withdraw')
            print('3. Balance')

            student_choice = int(input('Enter your selection (1,2 or 3): \n'))


            if student_choice == 1:
                  print('\n Processing....')
            deposite_amaount = int(input('\n Enter your amount to be deposited: '))
            if deposite_amaount < 1000:
                  print('\n Minimum amount to deposite is 1000')
            else:
                  account_balance += deposite_amaount
                  print(f" Dear student, you have deposited {deposite_amaount} and your account balance is {account_balance + deposite_amaount:}")


            if student_choice == 2:
                    print('\n Processing...')
                    withdraw_amount = int(input('Enter your amount to withdraw: '))

            if account_balance == 0:
                  print('Account balance is 0')
            elif withdraw_amount > account_balance:
                   print('Withdraw failed, insuffecient Funds')
            elif withdraw_amount < 500:
                  print('Minimum withdrw amount is 500, please try again')


            else: account_balance -= withdraw_amount
            print(f'you have successfuly withdrawn {withdraw_amount} and your account balance is {account_balance-withdraw_amount} ')

            if student_choice == 3:
                  print(f'\n Your accoutn balance is {account_balance:,}')
            else:
                  print('\n You have entered a wrong choice please select fro either 1,2 or 3')
              
            run = int(input("Enter 1 to continue or any number to exit:  "))

            if run!=1:
                  
                  print('Thanks for using our Sacco.')

Sacco_transaction()
                        





             
                  







