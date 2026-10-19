import datetime
import time
import math
import random
import uuid

from package import fileoperation
from package import calculation

def datetime_menu():

    while True:

        print("\n====================")
        print("Datetime and Time Operations")

        print("1. Display current date and time")
        print("2. Calculte Difference between two dates")
        print("3. Format date into custom Format")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Back to main menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            current = datetime.datetime.now()
            print("\nCurrent Date and time: ", current.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == 2:

            date1 = input("Enter the First date (YYYY-MM-DD): ")
            date2 = input("Enter the Second date (YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

            difference = abs((d2 - d1).days)
            print(f"Difference: {difference} days")

        elif choice == 3:

            date = datetime.datetime.now()
            print("\nFormatted Date:")
            print(date.strftime("%d-%m-%Y"))

        elif choice == 4:

            print("\nStopwatch started...")
            input("Press enter to stop the stopwatch.")
            print("Stopwatch stopped.")

        elif choice == 5:

            seconds = int(input("Enter countdown time in seconds: "))

            while seconds > 0:
                print("Time remaining: ", seconds)

                time.sleep(1)
                seconds = seconds - 1
                print("Countdown Finished!")

        elif choice == 6:
            break

        else:
            print("Invalid choice!")

def math_menu():

    while True:

        print("\n==============================")
        print("Mathematical Operations")
        print("==============================")

        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Areas of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            number = int(input("\nEnter a number: "))

            result = calculation.factorial(number)

            print("Factorial:", result)

        elif choice == 2:

            principal = float(input("\nEnter principal amount: "))
            rate = float(input("Enter rate of interest (in %): "))
            years = float(input("Enter time (in years): "))

            result = calculation.compound_interest(principal, rate, years)
            print("Compound Interest:", round(result, 2))

        elif choice == 3:

            angle = float(input("\nEnter angle in degrees: "))

            sin, cos, tan= calculation.trigonometric(angle)

            print("Sin:", sin)
            print("Cos:", cos)
            print("Tan:", tan)

        elif choice == 4:

            print("\n1. Circle")
            print("2. Rectangle")

            shape = int(input("Enter your choice: "))
            
            if shape == 1:

                radius = float(input("Enter radius: "))

                area = calculation.circle_area(radius)

                print("Area of Circle:", area)

            elif shape == 2:

                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = calculation.rectangle_area(length, width)

                print("Area of Rectangle:", area)

            else:

                print("Invalid choice!")

        elif choice == 5:

            break

        else:

            print("Invalid choice!")

def random_menu():

    while True:

        print("\n====================")
        print("Random Data Generation:")

        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to main menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            number = random.randint(1, 100)
            print("Random Number: ", number)

        elif choice == 2:

            numbers = []

            for i in range(5):
                numbers.append(random.randint(1, 100))
            
            print("Random Lists: ", numbers)

        elif choice == 3:

            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            length = int(input("Enter Password Length:"))

            password = ""

            for i in range(length):
                password = password + random.choice(characters)
            
            print("Generated Password: ", password)

        elif choice == 4:

            otp = random.randint(100000, 999999)
            print("Generated OTP: ", otp)

        elif choice == 5:
            break

        else:
            print("Invalid choice!")

def uuid_menu():

    print("\n====================")
    print("Generate Unique Identifiers:")
    
    unique_id = uuid.uuid4()

    print("Generated UUID: ", unique_id)

def file_menu():

    while True:

        print("\n====================")
        print("File Operations:")
        
        print("1. Create a new file")
        print("2. Write to a new file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to main menu")

        choice = int(input("Enter your choice:"))

        if choice == 1:

            filename = input("Enter File name: ")
            fileoperation.create_file(filename)

        elif choice == 2:

            filename = input("Enter File name: ")
            fileoperation.write_file(filename)

        elif choice == 3:

            filename = input("Enter File name: ")
            fileoperation.read_file(filename)

        elif choice == 4:

            filename = input("Enter File name: ")
            fileoperation.append_file(filename)

        elif choice == 5:
            break

        else:
            print("Invalid choice!")

def explore_module():

    print("\n====================")
    print("Explore Module Attributes:")

    module = input("Enter module name to explore: ")

    if module == "math":

        print("\nAvailable Attributes in math module: ")
        print(dir(math))

    elif module == "random":
    
            print("\nAvailable Attributes in random module: ")
            print(dir(random))

    elif module == "datetime":
    
            print("\nAvailable Attributes in datetime module: ")
            print(dir(datetime))

    else:
        print("Module not available in this program.")

def main():

    while True:

        print("\n====================")
        print("Welcome to Multi-Utility Toolkit")
        print("====================")

        print("Choose an option:")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File operation (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            datetime_menu()

        elif choice == 2:
            math_menu()

        elif choice == 3:
            random_menu()

        elif choice == 4:
            uuid_menu()

        elif choice == 5:
            file_menu()

        elif choice == 6:
            explore_module()

        elif choice == 7:

            print("\n====================")
            print("Thank You for using Multi-Utility Toolkit!")
            print("====================")

            break 

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()