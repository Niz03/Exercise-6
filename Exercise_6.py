# Write a program that receives a series of numbers from the user and allows the user to press the enter key to indicate that he or she is finished providing inputs. 
# After the user presses the enter key, the program should print the sum of the numbers and their average.

# Declaration of variables
sum = 0.0
avg = 0.0
count = 0

# Keeps looping, asking the user to input numbers. Stops if nothing is entered. Then converts int to float.
while True:
    sumInt = input("Enter a number, any number: ")
    count  += 1

    
    if sumInt == "":
        break
    
    sum += float(sumInt)
    avg = sum / count


# Final output.
print("The sum of all your numbers is: ", sum)
print("The average of your numbers is: ", avg)