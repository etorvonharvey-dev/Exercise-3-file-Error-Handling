stack = [ ]

while True:
    print("Stack menu")
    print("Add     (1)")
    print("History (2)")
    print("undo    (3)")
    print("exit    (4)")
    
    choice = input("Enter a choice: ")
    
    if choice == "1":
        value = input("Enter a value: ")
        stack.append(value)
        print("pushed value", value)
    elif choice == "2":
        print(stack)
    elif choice == "3":
        if len(stack) == 0:
            print("nothing")
        else:
            removed = stack.pop()
            print("undo", removed)
    elif choice == "4":
        print("game over")
        break