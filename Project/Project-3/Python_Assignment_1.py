a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))

if a>=b:
 if a>=c:
    max_num=a

 else:
      max_num=c

else:
   if b>=c:
      max_num=b

   else:
     max_num=c

print(f"The maxium number is: {max_num}")

     
