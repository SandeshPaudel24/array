# array =  []
# functions to write
# first ma array ko length shodcha input
# [array ko size determine vayo]  len(array) == length

# 1.addto arry [1,2] ma 3 add garda[1,2,3]  append
# 2.delete data[1,2,3,4,5] (1) chaidelete hunu  [slice spice pop ]
# 3.clear data  for loop launey delete
# 4. Display data for array data print hanney
# //clauses
# arraylaideko length vanda derai data add garna khojda  array full len(array) == length
# empty case delete handa empty dekhauchal en(array) <= 0


def operation(action, data, array):
    if action == "add":
        try:
            number = float(data)
            array.append(number)
            print("Number added successfully.")
        except ValueError:
            print("Invalid input")
    elif action == "delete":
        try:
            index = int(data)
            if 0 <= index < len(array):
                del array[index]
                print("Number deleted successfully.")
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid index")
    elif action == "clear":
        array.clear()
        print("Array cleared successfully.")
    elif action == "display":
        print("Current:", array)
    else:
        print("Invalid action.")


def arr():
    array1 = []
    while True:
        print("\n 1. add\n 2. delete\n 3. clear\n 4. display\n 5. exit")
        choice = input("Perform an operation: ")
        if choice == "1":
            if len(array1) >= 5:
                print("Limit exceeds")
            else:
                data = input("Enter a number: ")
                operation("add", data, array1)
            continue
        elif choice == "2":
            data = input("Enter an index to delete: ")
            operation("delete", data, array1)
        elif choice == "3":
            operation("clear", None, array1)
        elif choice == "4":
            operation("display", None, array1)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


arr()
