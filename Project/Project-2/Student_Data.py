print("Welcome to the Student Data Organizer!\n")
students={}

while True:
    print("Select an option:")
    print("1.Add student")
    print("2.Display All Students")
    print("3.Upadate Student Information")
    print("4.Delete Student")
    print("5.Display Subject Offered")
    print("6.Exit")

    Choice=int(input("Enter your choice:"))
    if(Choice==1):

        print("Enter student details:")
        staid=int(input("student ID:"))
        name=input("Name:")
        age=int(input("Age:"))
        grade=input("Grade:")
        dob=input("Date of birth (yyyy-MM-DD):")
        subject=input("subject(comma-separated):").split(",")

        st={
            "stid":stid,
            "name":name,
            "age":age,
            "grade":grade,
            "dob":dob,
            "subject":[s.strip()for s in subjects
        
        }
        students.append(st)
        print("\nstudent added sucessfully!\n")

        elif(Choice==2):
        print("\n---Display All Students---\n")

        if len(students)==0:
        print("No Details found!!")
        else:
        for info in students:
        print(
            f"Student ID:{info['staid']}|"
            f"Name:{info['name']}|"
            f"Age:{info['age']}|"
            f
        )

    
