
student_ids = []
student_names = []
student_ages = []
student_grades = []
student_dobs = []
student_subjects = []

print("welcome to the student Data Organizer!")

while True:

    print("\nselect an option:")
    print("1.Add student")
    print("2.Display All students")
    print("3.Upadate student information")
    print("4.Delete student")
    print("5.Display Subjects Offered")
    print("6.Exit")

    choice = input("Enter your choice:")

    # 1.Add studet
    if choice == "1":  

      print("\nEnter student details:")

      sid = input("student ID:")
      name = input("Name:")
      age = input("Age:")
      grade = input("Grade:")
      subjects = input("Subjects (comma-separeated):") 
      dob = input("Date of Birth (YYYY-MM-DD):")
      student_ids.append(sid)
      student_names.append(name)
      student_ages.append(age)
      student_grades.append(grade)
      student_dobs.append(dob)
      student_subjects.append(subjects) 
      print("student added successfully!")

    #2. Display All Students
    elif choice == "2":
          print("\n--- Display All students---")
  
          if len(student_ids) == 0:
              print("No students found.")
  
          else:
            for i in range(len(student_ids)):
                print("No student found.")
                print("\nstudent",i+1)
                print("Student ID:",student_ids[i])
                print("Name:", student_names[i])
                print("Age:", student_ages[i])
                print("Grade:", student_grades[i])
                print("Date of Birth:", student_dobs[i])
                print("subjects:", student_subjects[i])
                print("----------------------")

    #3. Update student
    elif choice =="3":

      sid = input("\nEnter student ID to update:")

      if sid in student_ids:

       index = student_ids.index(sid)

       print("\nEnter new information:")

       student_names[index]=input("Enter new name:")
       student_ages[index]=input("Enter new name:")
       student_grades[index]=input("Enter new Grade:")
       student_dobs[index]=input("Enter new Date of Birth(YYYY-MM-DD):")
       student_subjects[index]=input("Enter new Subjects:")

       print("Student updated successfully!")

      else:
         print("student ID not found.")

   #4.Delete Student
    elif choice == "4":

      sid= input("\nEnter student ID to delete:")

      if sid in student_ids:

         index = student_ids.index(sid)

         student_ids.pop(index)
         student_names.pop(index)
         student_ages.pop(index)
         student_grades.pop(index)
         student_dobs.pop(index)
         student_subjects.pop(index)

         print("student deleted successfully!")

      else:
         print("studentID not found.")

   #5.Display subjects
    elif choice =="5":

       print("\n--subjects offered--")
       print("Math,science,English,computer science,History")
       print("--------------------")
    
   #6. Exit
    elif choice =="6":

        print("\n Thank you for using the student Data Organizer!")
# `       print("Goodbye!")
        break

# # invalid choice
    else:
      print("\ninvalid choice!Please select between 1 and 6.")

   

         
   
            



 


