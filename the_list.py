# make a list to hold onto our items
the_list = []

def show_help():
    # print out instructions on how to use the app
    print("What do you want to add to the list?")
    print("""
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")
    
def show_list():
    # print out the list
    print("Here's your list:")
    
    for item in the_list:
        print(item)
        
def add_to_list(new_item):
    # add new items to our list
    the_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(the_list)))
    
show_help()

while True:
    # ask for new items
    new_item = input("> ")
    
    # be able to quit the app
        break
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()
