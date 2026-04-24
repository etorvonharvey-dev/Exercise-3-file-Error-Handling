stack = [ ]

while True:
    print("-----stack menu------")
    print("Push  (1)")
    print("pop   (2)")
    print("peek  (3)") 
    print("check (4)")
    print("stack (5)")
    print("Exit  (6)")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        value = input("Enter a value: ")
        stack.append(value)
        print("pushed", value)
        
    elif choice == "2":
        if len(stack) == 0:
            print("Stack in empty")
        else:
            print("Popped", stack.pop())
    elif choice == "3":
        if len(stack) == 0:
            print("stack is empty")
        else:
            print("Top Element", stack[-1])
    elif choice == "4":
        print("Is empty", len(stack) == 0)
    elif choice == "5":
        print(*stack)
    elif choice == "6":
        print("Exiting the stack")
        break 
    else:
        print("invalid")