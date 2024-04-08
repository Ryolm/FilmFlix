# Objectives
# Import all CRUD modules
import readrecords, addrecord, updaterecord, deleterecord, report

def read_file(file_path):
    try:
        with open(file_path, 'r') as open_file:
            rf = open_file.read()
            return rf
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")
        return ""

def films_menu():
    try:
        option = 0
        optionsList = ["1", "2", "3", "4", "5", "6"]

        menu_choices = read_file("dbMenu.txt")

        while option not in optionsList:
            print(menu_choices)
            option = input("Enter an option from the menu above: ")

            if option not in optionsList:
                print(f"{option} is not a valid choice")

        return option
    except FileNotFoundError as e:
        print(f"Error loading the menu: {e}")
        return "6"  # Default to exit option in case of error

mainProgram = True

while mainProgram:
    main_menu = films_menu()

    if main_menu == "1":
        readrecords.read_records()
    elif main_menu == "2":
        addrecord.insert_record()
    elif main_menu == "3":
        updaterecord.update_record()
    elif main_menu == "4":
        deleterecord.delete_record()
    elif main_menu == "5":
        report.search_report()
    elif main_menu == "6":
        mainProgram = False

input("Press Enter to exit...6")