"""
Author: Brandon Habib
Date: 1/21/2016
"""

#Initializing the array
numbers = []

#Initializing A
A = 0

#Printing instructions for the user
print ("Give me an integer Trevor and then type \"Done\" when you are done. When all is finished I will show you MAGIC!")

#A while loop to continue adding numbers to the array
while (A != "Done"):
    A = input ("Give me an integer Trevor --> ")
    #If statement appending the inputs
    if (A != "Done"):
        numbers.append(int(A))
        
#Initializing the Sum
Sum = 0

#Printing updates to the user
print ("MAGICING THE NUMBERS FORM THE ARRAY")

#For loop to sum the elements in the array numbers and prints number
for number in numbers:
    Sum = Sum + number
    print (number)

#Prints final message and the sum of numbers
print ("THIS IS THE MAGICAL SUM  " + str(Sum))
