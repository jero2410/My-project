# Program: This code has 6 programs that the user is going to choose which one he wants to use
# Authors: Mohamed Ayman and he solved problem 4 and problem 6
#          Mohand Salah and he solved problem 1 and problem 5
#          Jerome Nabil and he solved problem 2 and problem 3
# Version: version 3.0
# Date:    25/2/2024

# This is a function that calculates the grades by taking marks
def grades():
    print()
    print('***This program takes your mark and shows you the grade***')# welcome message and stats
    while True:
        try:# (try - except )function to prevent value errors
            mark = int(input('Please enter your mark: '))
            # Grade calculation based on mark range
            if (mark >= 90 and mark <= 100): # To set the marks over the 90 to A+
                print('Your grade is A+')
                break
            elif (mark >= 85 and mark < 90): # To set the marks between 85 and 90 to A
                print('Your grade is A')
                break
            elif (mark >= 80 and mark < 85): # To set the marks between 80 and 85 to B+
                print('Your grade is B+')
                break
            elif (mark >= 75 and mark < 80): # To set the marks between 75 and 80 to B
                print('Your grade is B')
                break
            elif (mark >= 70 and mark < 75): # To set the marks between 70 and 75 to C+
                print('Your grade is C+')
                break
            elif (mark >= 65 and mark < 70): # To set the marks between 65 and 70 to C
                print('Your grade is C')
                break
            elif (mark >= 60 and mark < 65): # To set the marks between 60 and 65 to D+
                print('Your grade is D+')
                break
            elif (mark >= 50 and mark < 60): # To set the marks between 50 and 60 to D
                print('Your grade is D')
                break
            elif (mark >= 0 and mark < 50): # To set the marks under the 50 to F
                print('Your grade is F')
                break
            else:
                print('Invalid number, please enter a valid number')
        except:# (try - except )function to prevent value errors
            print('Invalid number, please enter a valid number')


# Function to check Armstrong number
def armstrong_number_checker():
    print('\n***This program checks if a number is Armstrong or not***')# Welcome message and stats
    while True:
        try:# (try - except )function to prevent value errors
            num = input('Enter the number to check: ') # Take number of terms from user 
            n = len(num) # length of number = power
            # Initialize a counter and a total sum
            counter = 0
            total = 0
             # Iterate over each digit of the number
            while counter < n:
                individual_digit = int(num[counter])**n # Calculate the value of the current digit raised to the power of n
                total += individual_digit  # Add the value to the total sum
                counter += 1 # counter to Move to the next digit
            if total == int(num): # Check if the total sum is equal to the original number
                print('This number is an Armstrong number')  # If they are equal, print that the number is an Armstrong number
                print()
            else:
                print('This number is not an Armstrong number') # If they are not equal, print that the number is not an Armstrong number
                print()
            break # Exit the loop
        except:# (try - except )function to prevent value errors
            print('Invalid number, please enter a valid number')


# Function to calculate the approximate value of pi using Leibniz series
def The_German_mathematician_Leibniz():
    # Print a welcome message
    print("\n***This program takes the number of terms for mathematical operations and shows you the approximate value of pi***")
    while True:  # Start an infinite loop
        try:
            n = int(input('Enter the number of terms: ')) # Take num of terms from the user
             # Check if the number of terms is greater than 0
            if n>0: 
                den = 1
                Q_pi = 0
                counter = 0 # counter for positive term if counter is even and negative term if counter is odd
                while n > 0: # Iterate while there are still terms remaining
                    if counter%2 == 0: # If the counter is even, add the next term
                        Q_pi = Q_pi +(1/den)
                        # Update the denominator, decrease the number of terms, and increment the counter
                        den +=2
                        n -= 1
                        counter += 1
                    elif counter%2 != 0: # If the counter is odd, subtract the next term
                        Q_pi = Q_pi -(1/den)
                        # Update the denominator, decrease the number of terms, and increment the counter
                        den +=2
                        n -= 1
                        counter += 1
                # Print the approximate value of pi and pi itself
                print('π/4 ≅',Q_pi)
                print('π ≅ ',(Q_pi*4))
                print()
                break  # Exit the loop
            elif n <= 0:  # If the number of terms is not greater than 0, print an error message
                print('Invalid number, please enter a valid number')
        except:# (try - except )function to prevent value errors
            print('Invalid number, please enter a valid number')


# Function to encrypt text
def encryption():
    print('\n***This program takes text and encrypts it by shifting letters forward***')
    try:
        inp=input("Enter the phrase you want to encrypt: ") # Take phrase from the user
        while True:
            try:
                # Input to take the number of moves
                y=int(input("Enter how many moves you want for each letter: ")) # Take shifts from the user
                if y > 0:
                    break
                else:
                    print('Invalid number, please enter a valid number')
            except:
                print('Invalid number, please enter a valid number')
        x=""
        # Loop to change letters to their ASCII value and add moves and return them back 
        for i in inp:
            i=ord(i)
            if y >26: # To make him loop in numbers
              y-=26
            if (i >= 33 and i <= 64) or (i >= 91 and i <= 96) or (i >= 123 and i <= 127) or (i == 32) : # To keep every symbol and numbers and spaces without change
              x+=(chr(i))
            elif i>=97 and i+y <=122: # To add shifts on the ord number of the character in the phrase
              x+=(chr(i+y))  
            elif i+y>=90 and i+y>=91 : # To add shifts on the ord number of the character in the phrase and set the overflow to start from the first
              i -=26
              x+=(chr(i+y))
            elif i >=65 and i <=90: # To add shifts on the ord number of the character in the phrase
              x+=(chr(i+y))
            if i+y > 122: # To add shifts on the ord number of the character in the phrase and set the overflow to start from the first
              i -=26
              x+=(chr(i+y))
        print('The encrypted text:',x)
    except:
        print('Invalid number, please enter a valid number')


# Function to check if two lists have the same elements
def list_equal_checker():
    #this program checks if the two lists have the same elements
    print('\n***This program checks if two lists are similar or not***')
    while True:
        try:
            f_list=[] # Empty list to store user inputs 
            s_list=[] # Empty list to store user inputs 
            num_of_elements1 = int(input('Enter the number of elements of the first list: '))
            if num_of_elements1 <= 0:
                print('Invalid number, please enter a valid number')
                num_of_elements1 = int(input('Enter the number of elements of the first list: '))
            for i in range(0,num_of_elements1): # To set loop from 0 to number of elment in list that user enter
                while True:
                    try:
                        i = int(input('Enter the element: '))
                        f_list.append(i) # To add numbers in list
                        break
                    except:
                        print('Invalid number, please enter a valid number')
            print('first list =',f_list)
            f_list.sort() # To sort the element in the list
            num_of_elements2 = int(input('Enter the number of elements of the second list: '))
            if num_of_elements1 != num_of_elements2:
                print('lists are equal = False')
                break
            for i in range(0,num_of_elements2): # To set loop from 0 to number of elment in list that user enter
                while True:
                    try:
                        i = int(input('Enter the element: '))
                        s_list.append(i) # To add numbers in list
                        break
                    except:
                        print('Invalid number, please enter a valid number')
            print('second list =',s_list)
            s_list.sort() # To sort the element in the list
            if f_list == s_list: # To check if the lists are equal 
                print('lists are equal = True')
                break
            else:
                print('lists are equal = False')
                break
        except:
            print('Invalid number, please enter a valid number')


# Function to find factors of a positive integer
def integer_factors():
    print('\n***This program shows you all factors of a positive integer***')
    # Loop to ensure that the input is valid
    while True:
     # (try - except )function to preveny value errors
     try: 
        # Initialize an empty string to store factors
        factors = ""
        # Take the number from the user
        inp=int(input("Enter the number you want its factors: "))
        # Check how many numbers can divide our number
        if inp > 0:
            for i in range(1,inp+1):
             if inp%i==0:
              factors += str(i)+" , "
            # Remove the last two characters (comma and space) from factors
            factors = factors[:-2]
            # Print the factors
            print('The factors of',inp,':',factors)
            break
        elif inp <= 0:
            print('Invalid number, please enter a valid positive integer')
     except:# (try - except )function to preveny value errors
      print("Invalid number, please enter a valid positive integer")


# Main function to display menu and call functions based on user input
def main():
    print('\n***Hello and Welcome to our program***') #welcome message to the user 
    print('***Here you have a lot of programs to use***\n')
    while True:
        # display what in program
        print('\nJust select which program you want:') 
        print('1) Mark to grade')
        print('2) Armstrong number checker')
        print('3) The German mathematician Leibniz(π)')
        print("4) Text Encryption")
        print('5) Lists equal checker')
        print('6) Factors of positive integers')
        print('7) Exit program')
        choice = input()
        if choice == '1': # To choose program 1
            grades()
        elif choice == '2': # To choose program 2
            armstrong_number_checker() 
        elif choice == '3': # To choose program 3
            The_German_mathematician_Leibniz()
        elif choice == '4': # To choose program 4
            encryption()
        elif choice == '5': # To choose program 5
            list_equal_checker()
        elif choice == '6': # To choose program 6
            integer_factors()
        elif choice == '7': # To exit the main program
            print('Thanks for using our program ☺')
            break
        else:
            print('Invalid choice, please enter a valid choice: ')# if user input wrong input


# Call the main function to start the program
main()
