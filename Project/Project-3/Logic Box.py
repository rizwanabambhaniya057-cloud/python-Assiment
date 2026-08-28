print("welcome to the pattern Generator and Number Analyzer!")

while True:
    print("\n1. Generate a pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit\n")

    choice = int(input("select an option:"))

    match choice:

        case 1:
            rows = int(input("Enter the number of rows foe pattern:"))
            print("Pattern:")
            for i in range(1,rows+1):
                print("*",end=" ")
            print()

        case 2:
            num1 =int(input("Enter the start of range:"))
            num2 =int(input("Enter the end of range:"))
            sum = 0

            for k in range(num1, num2+1):
                if k % 2 == 0:
                    print(f"Number {k} is Even")

                else:
                    print (f"Number {k} is odd")

                for i in range (num1,num2 + 1):
                    sum= sum+1

                print(f"sum of all numbers from {num1} to {num2} is:",sum)

        case 3:
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Invalid Input")
    

    
                
                
