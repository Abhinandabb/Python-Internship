a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
ch=0
while ch<5:
    print("Calculator menus:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Addition is:", a+b)
    elif choice==2:
        print("Subtraction is:", a-b)
    elif choice==3:
        print("Multiplication is:", a*b)
    elif choice==4:
        if b != 0:
            print("Division is:", a/b)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice==5:
        print("Exiting the calculator.")
        break
    else:
        print("Invalid choice")