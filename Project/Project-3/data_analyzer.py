print("welcome to the Data Analyzer and Transformer program")

data = []

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def display_summary():
    if not data:
        print("nplease input data first.")
        return
    print("\nData Summary:")
    print("-Total elements:",len(data))
    print("-Minimum value:",min(data))
    print("-Maximum value:",max(data))
    print("-Sum of all values:",sum(data))
    print("-Average value:", round(sum(data) / len(data), 2))

def dataset_statistics():
        minimum = min(data)
        maximum = max(data)
        total   = sum(data)
        average = total/ len(data)
        return minimum,maximum,total,average

while True:
        print("\nMain Menu:")
        print("1.Input Data")
        print("2.Display Data Summary(Built-in Functions)")
        print("3.Caluculate Factroial(Recursion)")
        print("4.Filter Data by Threshold(Lambda Function)")
        print("5.Sort Data")
        print("6.Display Dataset Statistics(Return Multiple Values)")
        print("7.Exit program")

        choice = int(input("Please enter your choice"))

        # step 1:Input Data
        if choice == 1:
            values = input("\nEnter data for a 1D array(separated by spaces):")
            data = list(map(int,values.split()))
            print("Data loaded successfully!")

        # Step 2: Display_summary()
        elif choice == 2:
         display_summary

         # Step 3: Factorial
        elif choice == 3:
            n = int(input("\nEnter a number to calculate its factorial:"))
            if n < 0:
             print("Factorial is not defined for negative numbers.")

            else:
                result = factorial(n)
                print("\nFactorial of {n} is: {result}")

        # Step 4:Filter using Lambda 
        elif choice==4:
            if len(data)== 0:
                print("\nPlease input data first.")

            else:
                threshold= int(input("\nEnter a threshold value to filter out data above this:"))
                filtered = list(filter(lambda x: x >= threshold, data))
                print(f"\nFiltered Data (Values >= {threshold}):")
                print(*filtered, sep=",")

            #Step 5:Sort Data
        elif choice == 5:
            if len(data) == 0:
                print("\nPlease input data first.")

            else:
                print("\nChoose sorting option:")
                print("1.Ascending")
                print("2.Descending")
                sort_choice = int(input("\nEnter your choice:"))
                if sort_choice == 1:
                    sorted_data = sorted(data,reverse=True)

                    print("\nSorted Data in Ascending Order:")
                    print(*sorted_data, sep=",")

                else:
                    print("\nInvalid sorting choice.")

             #Step 6:Statistics
        elif choice == 6:
            if len(data)==0:
                print("\nPlease input data first.")

            else:
                minmum,maximum,total,average=dataset_statistics()
                print("\nDataset Statistics:")
                print ("-Minimum value:,minimum")
                print ("-Maximum value:,maximum")
                print ("-Sum of all values:,Total")
                print ("-Average value:,round (average,2)")

             #Step 7:Exit
        elif choice == 7:

            print("\nThank you for using the Data Analyzer and"
                  "Transformer program. Goodbye!"
                  )
            break

        else:

            print("\ninvalid choice.Please try again.")
                



        



            

    
        
