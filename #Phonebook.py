#Phonebook

actions = 'show,delete,add,exit'

phonebook = {
    'Jona': '01534 72394 927',
    'Jesper': '01534 45439 226',
    'Ali': '01534 21235 424',
    'Ivan': '01534 81238 483',
    'Claudia': '01534 94667 862',
}

name_list = ['Jona', 'Jesper', 'Ali', 'Ivan', 'Claudia']

while True:
    action = input("Which action would you like to perform? (show, delete, add, exit): ").strip().lower()

    if action in actions:
        if action == 'show':
            print("\nCurrent contacts:", name_list)
            name = input("Whose phone number would you like to see? ").strip()
            if name in name_list:
                print(f"The phone number of {name} is {phonebook[name]}")
            else:
                print("This contact does not exist in the phonebook.")

        elif action == 'delete':
            print("\nCurrent contacts:", name_list)
            name = input("Which contact would you like to delete? ").strip()
            if name in name_list:
                del phonebook[name]
                name_list.remove(name)
                print(f"{name} has been successfully deleted.")
                print("Updated contacts:", name_list)
            else:
                print("This name is not in the phonebook. Please try again.")

        elif action == 'add':
            name_to_add = input("Enter the name of the new contact: ").strip()
            number_to_add = input(f"Enter the phone number for {name_to_add}: ").strip()
            phonebook[name_to_add] = number_to_add
            if name_to_add not in name_list:
                name_list.append(name_to_add)
            print(f"{name_to_add} was added successfully.")
            print("Updated phonebook:", phonebook)

        elif action == 'exit':
            confirm = input("Are you sure you want to exit? (Yes/No): ").strip().lower()
            if confirm == 'yes':
                print("Goodbye!")
                break
            else:
                print("Continuing with the phonebook...")

    else:
        print("Invalid action. Please choose from: show, delete, add, exit.")