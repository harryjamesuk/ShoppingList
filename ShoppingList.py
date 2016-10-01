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
        print(numbered_shopping_list)
    else:
        print(', '.join(shopping_list) + ".")


def askToReplace():
    print("What would you like to replace? Provide item position or name.")
    item_to_replace = input("> ")
    print("Ok, we'll replace", item_to_replace + ". What should we replace it with?")
    print("Provide item name.")
    item_to_replace_with = input("> ")
    print("Attempting to replace...")
    replaceItem(item_to_replace, item_to_replace_with)
    print()
    printShoppingList(False)

def askToDelete():
    print("What would you like to delete? Provide item position or name.")
    item_to_delete = input("> ")
    print("Ok, we'll delete", item_to_delete)
    print("Attempting to delete...")
    deleteItem(item_to_delete)
    print()
    printShoppingList(False)

def askToGetpos():
    print("What item are you looking for?")
    item_to_find = input("> ")
    print("Ok, we'll look for", item_to_find)
    print("Searching...")
    getpos(item_to_find)
    print()
    printShoppingList(True)

def askToPrintPos():
    print("What is the position of the item you are looking for?")
    item_to_print = input("> ")
    if item_to_print[0].isdigit():
        printpos(item_to_print)
    else:
        print("### ERROR ###")
        print("Please specify the numerical position of the item you are looking for.")
        askToPrintPos()
    print()
    printShoppingList(False)

def selectMenuOption():
    print("What would you like to do?")
    # Print menu
    for menuOption in menu:
        print("-", menuOption[0] + ":", menuOption[1])

    active_menu_option = input("> ").lower().strip()

    if active_menu_option == "replace":
        # Replace
        askToReplace()
    elif active_menu_option == "delete":
        # Delete
        askToDelete()
    elif active_menu_option == "getpos":
        # Getpos
        askToGetpos()
    elif active_menu_option == "printpos":
        # Printpos
        askToPrintPos()
    else:
        # Unknown - Ask again
        print("Unknown menu option selected:", active_menu_option + ".", "Please try again: \n")
        selectMenuOption()


def returnIndexFromUserInput(user_input):
    user_input = user_input.strip()
    for i in range(len(user_input)-1):
        if i == 0:
            index = user_input[i]
        else:
            index += user_input[i]
    if user_input[0].isdigit():
        index = int(user_input)-1 # Convert to int, remove additional characters, and remove 1 to get index.
        if index < 0:
            print("### ERROR ###")
            print("The number you have specified is not a valid position in the shopping list. The shopping list",
                  "starts from 1")
            return False
        elif index > len(shopping_list):
            print("### ERROR ###")
            print("The number you have specified is not a valid position in the shopping list. The shopping list",
                  "has a length of:", str(len(shopping_list)))
            return False
        else:
            return index
    else:
        # String index
        indexes = []
        current_index = 0
        for item in shopping_list:
            if item == user_input:
                indexes.append(current_index)
            current_index+=1
        if len(indexes) == 0:
            print("No indexes found for specified selection.")
        return indexes


def replaceItem(item, replacement):
    global shopping_list
    index = returnIndexFromUserInput(item)
    if isinstance(index, bool):
        # We've hit an error!
        print("Please try again:")
        askToReplace()
    elif isinstance(index, int):
        shopping_list[index] = replacement
    elif isinstance(index, list):
        for i in index:
            shopping_list[i] = replacement


def deleteItem(item):
    global shopping_list
    index = returnIndexFromUserInput(item)
    if isinstance(index, bool):
        # We've hit an error!
        print("Please try again:")
        askToDelete()
    elif isinstance(index, int):
        del shopping_list[index]
    elif isinstance(index, list):
        for i in index:
            del shopping_list[i]


def getpos(item):
    global shopping_list
    index = returnIndexFromUserInput(item)
    if isinstance(index, bool):
        # We've hit an error!
        print("Please try again:")
        getpos()
    elif isinstance(index, list):
        for i in index:
            print("- Found:", item, "at position:", i + 1)


def printpos(item):
    global shopping_list
    index = returnIndexFromUserInput(item)
    if isinstance(index, bool):
        # We've hit an error!
        print("Please try again:")
        askToDelete()
    elif isinstance(index, int):
        print("The item at position:", index+1, "is:", shopping_list[index])

# Startup
name = input("What is your name? ")
print("\n\n")

# Welcome
print("Welcome,", name + ".")
printShoppingList(False)
print("")
selectMenuOption()
