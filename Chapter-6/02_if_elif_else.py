age=int(input("Enter the age:"))

if(age>=18):
  print("Eligible")

elif(age<=0):
  print("You have entered Invalid Age")
else:
  print("Not Eligible")

print("yes") if age>18 else print("No")