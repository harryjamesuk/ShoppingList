shopping_list = ["Kraves", "Nutella", "Chocolate", "Pancakes", "Ice-cream", "Sugar", "Bread", "Pan au chocolat",
                "Teabags", "Milk"]
menu = [["Add", "Appends an item to the end of the shopping list"],
        ["Delete", "Deletes the item(s) at specified integer or value"],
        ["Replace", "Replaces the item(s) at specified integer or value"],
        ["Getpos", "Gets the item positions with specified value"],
        ["Printpos", "Prints the item at specified integer"],
        ["Exit", "Terminates the program"]]


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


def askToAdd():
    print("What would you like to add? Provide item name.")
    item_to_add = input("> ").strip()
    print("Attempting to add item...")
    if not addItem(item_to_add):
        return False
    print("- Successfully added \"" + item_to_add + "\" to your Shopping List! :)")
    print("Press ENTER to continue...")
    input("> ")
    print("\n\n\n")
    printShoppingList(False)


def askToDelete():
    print("What would you like to delete? Provide item position or name.")
    item_to_delete = input("> ").strip()
    print("Attempting to delete...")
    if not deleteItem(item_to_delete):
        return False
    print("- Successfully deleted \"" + item_to_delete + "\" from your Shopping List! :)")
    print("Press ENTER to continue...")
    input("> ")
    print("\n\n\n")
    printShoppingList(False)


def askToReplace():
    print("What would you like to replace? Provide item position or name.")
    item_to_replace = input("> ")
    print("Ok, we'll replace", item_to_replace + ". What should we replace it with?")
    print("Provide item name.")
    item_to_replace_with = input("> ").strip()
    print("Attempting to replace...")
    if not replaceItem(item_to_replace, item_to_replace_with):
        return False
    print("- Successfully replaced \"" + item_to_replace + "\" with \"" + item_to_replace_with + "\"! :)")
    print("Press ENTER to continue...")
    input("> ")
    print("\n\n\n")
    printShoppingList(False)


def askToGetpos():
    print("What item are you looking for? Provide item name. [PRESS 'z' TO EXIT LOOP]")
    item_to_find = input("> ").strip()
    if item_to_find.lower() == 'z':
        print("Ok - exiting loop...")
        print("\n\n\n")
        return False
    print("Ok, we'll look for", item_to_find)
    print("Searching...")
    if not getpos(item_to_find):
        return False
    print("Press ENTER to continue...")
    input("> ")
    print("\n\n\n")
    printShoppingList(False)
    askToGetpos()


def askToPrintPos():
    print("What is the position of the item you are looking for? Provide item position. [PRESS 'z' TO EXIT LOOP]")
    item_to_print = input("> ").strip()
    if item_to_print.lower() == 'z':
        print("Ok - exiting loop...")
        print("\n\n\n")
        return False
    if item_to_print[0].isdigit():
        if not printpos(item_to_print):
            return False
    else:
        print("### ERROR ###")
        print("Please specify the numerical position of the item you are looking for.")
        askToPrintPos()
        return False
    print("Press ENTER to continue...")
    input("> ")
    print("\n\n\n")
    printShoppingList(False)
    askToPrintPos()


def selectMenuOption():
    print("What would you like to do?")
    # Print menu
    for menuOption in menu:
        print("-", menuOption[0] + ":", menuOption[1])

    active_menu_option = input("> ").lower().strip()

    if active_menu_option == "add":
        # Add
        printShoppingList(False)
        askToAdd()
    elif active_menu_option == "delete":
        # Delete
        printShoppingList(True)
        askToDelete()
    elif active_menu_option == "replace":
        # Replace
        printShoppingList(True)
        askToReplace()
    elif active_menu_option == "getpos":
        # Getpos
        askToGetpos()
    elif active_menu_option == "printpos":
        # Printpos
        askToPrintPos()
    elif active_menu_option == "exit" or active_menu_option == "z" or active_menu_option == "quit":
        # Exit
        quit()
    else:
        # Unknown - Ask again
        print("Unknown menu option selected:", active_menu_option + ".", "Please try again: \n")
    selectMenuOption()


def returnIndexFromUserInput(user_input):
    user_input = user_input.strip()
    if user_input[0].isdigit():
        # Positional index
        for i in range(len(user_input)):
            if user_input[i].isdigit():
                if i == 0:
                    index = user_input[i]
                else:
                    index += user_input[i]
        index = int(index)-1  # Convert to int and remove 1 to get index.
        if index < 0:
            print("### ERROR ###")
            print("The number you have specified is not a valid position in the shopping list. The shopping list",
                  "starts from 1")
            return False
        elif index >= len(shopping_list):
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
            if item.lower() == user_input.lower():
                indexes.append(current_index)
            current_index+=1
        if len(indexes) == 0:
            #print("No indexes found for specified selection.")
            #Let's be user friendly.
            print("Sorry! We couldn't find: " + user_input + " in your shopping list :'(")
            return False
        return indexes


def addItem(item):
    global shopping_list
    if any(char.isdigit() for char in item):
        print("### ERROR ###")
        print("Invalid usage: Please specify the name of the item you want to add.")
        askToAdd()
        return False
    elif isinstance(item, str):
        shopping_list.append(item)
        return True
    return False  # No if's reached.


def deleteItem(item):
    global shopping_list
    index = returnIndexFromUserInput(item)
    if isinstance(index, bool):
        # We've hit an error!
        print("Please try again:")
        askToDelete()
        return False
    elif isinstance(index, int):
        del shopping_list[index]
        return True
    elif isinstance(index, list):
        for i in sorted(index, reverse=True):  # Ignore this error.
            del shopping_list[i]
        return True
    return False  # No if's reached


def replaceItem(item, replacement):
    global shopping_list
    replacementContainsDigit = False
    for character in replacement:
        if character.isdigit():
            replacementContainsDigit = True

    if replacementContainsDigit:
        # Error - Replacement contains digits.
        print("### ERROR ###")
        print("Your replacement must be text, not a number.")
        print("Try again:")
        return False

    index = returnIndexFromUserInput(item)
    if isinstance(index, bool):
        # We've hit an error!
        print("Please try again:")
        askToReplace()
        return False
    elif isinstance(index, int):
        shopping_list[index] = replacement
        return True
    elif isinstance(index, list):
        for i in index:
            shopping_list[i] = replacement
        return True
    return False  # No if's reached


def getpos(item):
    global shopping_list
    index = returnIndexFromUserInput(item)
    if isinstance(index, bool):
        # We've hit an error!
        print("Please try again:")
        askToGetpos()
        return False
    elif isinstance(index, int):
        # Error - Specify value, not int.
        print("### ERROR ###")
        print("You can't get the position of something that you already know the position of!")
        print("Please try again:")
        askToGetpos()
        return False
    elif isinstance(index, list):
        for i in index:
            print("- Found:", item, "at position:", i + 1)
        return True
    return False  # No if's reached


def printpos(item):
    global shopping_list
    index = returnIndexFromUserInput(item)
    if isinstance(index, bool):
        # We've hit an error!
        print("Please try again:")
        askToPrintPos()
        return False
    elif isinstance(index, int):
        print("The item at position:", index+1, "is:", shopping_list[index])
        return True
    return False  # No if's reached

# Startup
name = input("What is your name? ")
print("\n\n")

# Welcome
print("Welcome,", name + ".")
printShoppingList(False)
print("")
selectMenuOption()
