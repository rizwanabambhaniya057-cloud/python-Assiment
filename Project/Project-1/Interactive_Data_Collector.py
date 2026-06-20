print("welcome to the interactive personal Data Collector!",end="\n\n")

Name=input("please enter your name:")
Age=int(input("please enter your age:"))
Height=float(input("please enter your height in meters:"))
Favourite_Number=int(input("please enter your favourite number:"))
print(end="\n")

print("Thank you! Here is the information we collected:",end="\n\n")

print("Name:",Name,"Type:",type(Name),"ID:",id(Name))
print("Age:",Age,"Type:",type(Age),"ID:",id(Age))
print("Height:",Height,"Type:",type(Height),"ID:",id(Height))
print("Fav No:",Favourite_Number,"Type:",type(Favourite_Number),"ID:",id(Favourite_Number))
print(end="\n")

current_year=2026

year_age=current_year-Age

print("Your birth year is approximately:",year_age,)
print("Thank you for using the personal Data Collector.Goodbye!")



    


 



