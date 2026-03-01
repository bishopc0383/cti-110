#Coreonte Bishop
#2/27/2026
#P1HW2
#using input and print

#Pseudocode:
#1. Display message explaining what the code does
#2. Ask user to enter their budget
#3. Ask user to enter travel destination
#4. Ask user for amount they will spend on gas
#5. Ask user for amount they will spend on accommodation
#6. Ask user for amount they will spend on food
#7. Add expenses together
#8. Subtract expenses from budget
#9. Display results

print("This program calculates and displays travel expenses\n")
print()

#Ask user for budget
budget = int(input("Enter Budget: "))
print()

#Ask for destination
destination = input("Enter your travel destination: ")
print()

#Ask for gas expense
gas = int(input("How much do you think you will spend on gas? "))
print()

#Ask for accommodation expense
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()

#Ask how much will be spent on food
food = int(input("Last, how much do you need for food? "))
print()

#add expenses
total_expenses = gas + accommodation + food
print()

#subtract expenses from budget
remaining_balance = budget - total_expenses
print()

#Display results
print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)
