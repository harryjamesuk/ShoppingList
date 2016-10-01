shopping_list = ["Kraves", "Nutella", "Chocolate", "Pancakes", "Ice-cream", "Sugar", "Bread", "Pan au chocolat",
                "Teabags", "Milk"]
# TODO: Add add functionality
menu = [["Replace", "Replaces the item(s) at specified integer or value"],
        ["Delete", "Deletes the item(s) at specified integer or value"],
        ["Getpos", "Gets the item positions with specified value"],
        ["Printpos", "Prints the item at specified integer"]]


# Defs
def printShoppingList(show_positions):
    print("Your shopping list right now is: ")
    if show_positions:
        numbered_shopping_list = ""
        i = 1
        for item in shopping_list:
            numbered_shopping_list += "(" + str(i) + ") " + item + ". "
            i += 1
    else:
        print(', '.join(shopping_list) + ".")


def selectMenuOption():
    print("What would you like to do?")
    # Print menu
    for menuOption in menu:
        print("-", menuOption[0] + ":", menuOption[1])

    active_menu_option = input("> ").lower().strip()

    if active_menu_option == "replace":
        # Replace
        print("What would you like to replace? Provide item position or name.")
        item_to_replace = input("> ")
        print("Ok, we'll replace", item_to_replace + ". What should we replace it with?")
        print("Provide item name.")
        item_to_replace_with = input("> ")
        print("Attempting to replace...")
        replaceItem(item_to_replace, item_to_replace_with)
        print("Replaced!")
        printShoppingList(False)
    elif active_menu_option == "delete":
        # Delete
        print("Coming soon.")
    elif active_menu_option == "getpos":
        # Getpos
        print("Coming soon.")
    elif active_menu_option == "printpos":
        # Printpos
        print("Coming soon.")
    else:
        # Unknown - Ask again
        print("Unknown menu option selected:", active_menu_option + ".", "Please try again: \n")
        selectMenuOption()


# Have not tested
def returnIndexFromUserInput(user_input):
    user_input = user_input.strip()
    if user_input[0].isDigit():
        index = int(user_input[0])-1 # Convert to int, remove additional characters, and remove 1 to get index.
        if index < 0:
            print("### ERROR ###")
            print("The number you have specified is not a valid position in the shopping list. The shopping list"
                  "starts from 1")
        elif index > len(shopping_list):
            print("### ERROR ###")
            print("The number you have specified is not a valid position in the shopping list. The shopping list"
                  "has a length of:", str(len(shopping_list)))
        else:
            return index
    else:
        # String index
        indexes = []
        currentIndex = 0
        for item in shopping_list:
            if item == user_input:
                indexes.append(currentIndex)
            currentIndex+=1


def replaceItem(item, replacement):
    global shopping_list
    if item[0].isdigit():
        item = int(item[0])-1 # Convert to int, remove additional characters, and remove 1 to get index.
        shopping_list[item] = replacement
    else:
        shopping_list = [shopping_list_item.replace(item, replacement) for shopping_list_item in shopping_list]


def deleteItem(item):
    global shopping_list
    if item[0].isdigit():
        item = int(item[0])

# Startup
name = input("What is your name? ")
print("\n\n")

# Welcome
print("Welcome,", name + ".")
printShoppingList(False)
print("")
selectMenuOption()
