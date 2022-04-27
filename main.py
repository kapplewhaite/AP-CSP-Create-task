# Created by Kaiden Applewhaite
# 4/22/2022

# Import the os module to clear the console from time to time
import os

# Import the sleep function to pause the program
from time import sleep

# Defines the command to clear the console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Defines the function to print the contents of each dictionary
def showInventory(department:dict):
    """Takes each key from a given dictionary and prints it"""
    for k in department:
        # Prints the key with the value as a price
        print(k + ': $' + str(department[k]))

# Defines the function to display an error message
def showError():
    print('This command was unable to be fulfilled.')
    print('Please try again')
    print('This message will disappear in 3 seconds...')
    sleep(3)
  
  
# The user's empty shopping list at the start of the program
shoppingList = []

# Sets the user's subtotal to $0.00
subtotal = 0.0

# The dictionaries containing all of the products
# Each item in categorized into a particular dictionary that corresponds to where you would find it in a store
meat = {
    'chicken': 8.20,
    'beef': 5.49,
    'pork': 3.99
}

produce = {
    'bananas': 0.21,
    'apples': 0.75,
    'grapes': 4.98,
    'oranges': 0.79,
    'strawberries': 2.99, # 1lb container
    'potatoes': 0.89,
    'tomatoes': 0.56,
    'onions': 0.50,
    'carrots': 2.49, # 2lb bag
    'lettuce': 1.79,
    'bell peppers': 0.99,
    'garlic': 0.50
}

dairy = {
    'milk': 3.99, # 1 gal jug
    'cheese': 2.00, # 8oz block
    'ice cream': 2.50 # 48fl oz container
}

other = {
    'bread': 1.49,
    'eggs': 2.98, # 18ct 
    'salt': 1.19, # 26oz shaker
    'pepper': 4.79, # 4oz shaker
    'ketchup': 1.25, # 24oz bottle
    'mayonnaise': 3.19 # 30fl oz jar
}

# Starts the main program
print('Welcome to the shopping list planner!')

# As a test, print out each of the 4 dictionaries (This should be commented out during the final project)
# print(meat)
# print(produce)
# print(dairy)
# print(other)

# Initialize a loop to start the program
while True:
    print('There are ' + str(len(shoppingList)) + ' items on your shopping list.')
    print('What you would like to do? (search, view list, done)')
    userChoice = input('Type your choice (case-sensitive): ')

    # Branches into multiple different paths depending on the user's choice

    # If the user chooses search, they will have the opportunity to search through the 4 different dictionaries for products to add to their list
    # If the user chooses to view their list, the program will show off of the items in the list and provide the subtotal at the end
    # If the user selects done, this will break the loop and print the list to a text file. Sales tax will also be calculated and added to the file. Please note that this option will only be available if the shopping list contains items.

    # Clear the console to free up space
    clearConsole()

    if userChoice == 'search':
        # Prompts the user with which department they want to search through
        print('Which department would you like to view (meat, produce, dairy, other)')
        userChoice = input('Type your choice (case-sensitive): ')

        if userChoice == 'meat':
            print("Here's the meat department: ")

            # Prints the meat department
            showInventory(meat)
          
            # Asks the user which item from the dictionary they would like to purchase
            print('Which item would you like to purchase?')
            userChoice = input()

            # If the item cannot be found in the dictionary, inform the user and restart the loop
            if userChoice not in meat:
                showError()
            # If the item was able to be found in the dictionary, add it to the shopping list and add the price to the subtotal
            else:
                shoppingList.append(userChoice)
                subtotal += meat[userChoice]

            clearConsole()

        elif userChoice == 'produce':
            print("Here's the produce department: ")

            # Prints the produce department
            showInventory(produce)

            # Asks the user which item from the dictionary they would like to purchase
            print('Which item would you like to purchase?')
            userChoice = input()

            # If the item cannot be found in the dictionary, inform the user and restart the loop
            if userChoice not in produce:
                showError()
            # If the item was able to be found in the dictionary, add it to the shopping list and add the price to the subtotal
            else:
                shoppingList.append(userChoice)
                subtotal += produce[userChoice]

            clearConsole()

        elif userChoice == 'dairy':
            print("Here's the dairy department: ")

            # Prints the dairy department
            showInventory(dairy)

            # Asks the user which item from the dictionary they would like to purchase
            print('Which item would you like to purchase?')
            userChoice = input()

            # If the item cannot be found in the dictionary, inform the user and restart the loop
            if userChoice not in dairy:
                showError()
            # If the item was able to be found in the dictionary, add it to the shopping list and add the price to the subtotal
            else:
                shoppingList.append(userChoice)
                subtotal += dairy[userChoice]

            clearConsole()

        elif userChoice == 'other':
            print("Here are some other items for sale: ")

            # Prints the other department
            showInventory(other)

            # Asks the user which item from the dictionary they would like to purchase
            print('Which item would you like to purchase?')
            userChoice = input()

            # If the item cannot be found in the dictionary, inform the user and restart the loop
            if userChoice not in other:
                showError()
            #If the item was able to be found in the dictionary, add it to the shopping list and add the price to the subtotal
            else:
                shoppingList.append(userChoice)
                subtotal += other[userChoice]

            clearConsole()

        # If the provided answer doesn't match with the provided answers, inform the 
        else:
            showError()
            clearConsole()

    elif userChoice == 'view list':
        # Shows each item currently on the list
        clearConsole()
        
        