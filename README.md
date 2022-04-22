# AP-CSP-Create-task
A public repository containing the code for my AP Computer Science Principles Create Performance Task

## Create Performance Task Idea
This is a text-based grocery shopping planner that will organize your items into a list and calculate their price as well

## How it works:
At the start of the program, a while loop will begin that will ask the user what type of item they would like to shop for (meat, produce, dairy). The program will then provide each item under that type available for purchase, as well as their price. If an item requires weight to calculate price (ie. $x/lb), this will be noted next to the price and the user will be asked to provide a quantity for that item.

Once the user has provided the necessary information, the item will be added to the user's 'shopping list', as well as their 'receipt'. The price will be added to the subtotal to be calculated with taxes for the final total.

The selection process will continue until the user notes that they are finished shopping. At this point, everything in the shopping list will be printed to a text file as a receipt. The total of the cart will be calculated to include tax.

## Outputs:
This program will output a text file titled 'receipt.txt'. The file will contain each item in a user's shopping list as well as the price for each item, the subtotal of the cart, and the final total of the cart.