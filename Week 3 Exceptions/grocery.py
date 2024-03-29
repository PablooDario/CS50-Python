# Implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.

def main():
    items = grocery_list()
    
    print()
    for key in sorted(items.keys()):
        print(items[key], key)
    
def grocery_list():
    # Create Dictionary
    items = dict() 
    # Prompr user for an item
    while True:
        try:
            item = input().upper()
        # If the user doesn't prompt nothing the while lopp finish
        except EOFError:
            return items
        # Count the items
        try:
            items[item] +=1
        except KeyError:
            items[item] = 1
        
main()