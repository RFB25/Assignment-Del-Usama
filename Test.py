# set the items the store sells
shopItems = [
    {
        "item": "Beans",
        "price": 1000,
    },
    {
        "item": "Rice",
        "price": 200,
    },
    {
        "item": "Garri",
        "price": 30,
    },
    {
        "item": "Yam",
        "price": 50,
    },
]

# Store the default option for the store to not quit till the user quits by hand
exitStore = 'n'

# set default variable to hold the items the customer will select
selectedItems = []

# set the default total
total = 0

while exitStore != "y":

    # introduce the application
    print("Select the shop items you want to buy:")

    # list the whole items
    for item in shopItems:
        index = shopItems.index(item)
        print(index, item['item'], "= NGN", item['price'])

    # ask the user for choice
    userChoice = int(input('Choose Item: '))  # cast the decision to int

    # add the chosen item to the selected list
    selectedItems.append(shopItems[userChoice])

    # notify the user of the action taken
    print("Added", shopItems[userChoice]['item'], "to Cart")

    # calculate total cart worth
    for item in selectedItems:
        total += item['price']

    print("Total Items in cart", len(selectedItems))
    print('Total Worth Cart NGN', total)

    # ask if user wants to quit the application
    exitStore = input('Do you want to quit the store (y/n): ')

# print friend exit message
print('Please tender NGN', total, 'To the cashier')
print('Thank you... Please come again !!!')

# program end
