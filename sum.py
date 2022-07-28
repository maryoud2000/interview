def sum(num1, num2, num3):
    if (num1 + num2 == num3):
        print("equal") 

    elif (num1 and num2 == num3):
         print("All numbers are equal")

    elif (num1 and num2 != num3):
        print("All numbers not equal")
    
    else:
        print("OTHER")

sum(1, 2, 3)

# # Store input numbers
# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')

# # Add two numbers
# sum = float(num1) + float(num2)

# # Display the sum
# print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))