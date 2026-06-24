print("Welcome to the pattern Generator and Number Analyzer!\n")


while True:
    print("Select an option:")
    print("1. Generate a pattern")
    print("2. Analyzer a Range of Numbers")
    print("3. Exit")

    choice=int(input("Enter your choice"))

    if choice==1:
       no_of_rows=int(input("Enter the number of rows the pattern:"))

       print("\nPattern:")
       for i in range(1,no_of_rows+1):
             print("*"*i)

       print("\n")
    
    elif choice==2:
       start=int(input("Enter the end of the range:"))
       end=int(input("Enter the end of the range:"))
       sum=0
       for i in range(start,end+1):
           if i%2==0:
               print("Number",i,"is Even")
           else:
               print("Number",i,"is odd")
               sum+=i
               print("Sum of all number from",start,"to",end,"is:",sum)
               print("\n")

    elif choice==3:
            print("Exiting the program. Goodbye!")
            break
       
    else:
        print("Invalid choice!!!")
                 

