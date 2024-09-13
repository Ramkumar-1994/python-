marks1=int(input("Enter Marks 1:"))
marks2=int(input("Enter Marks 2:"))
marks3=int(input("Enter Marks 3:"))

total_percentage=((marks1+marks2+marks3)/300)*100
print(total_percentage)

if(marks1>33 and marks2>33 and marks3>33):
  if(total_percentage>=40):
    print("You are passed")

  else:
    print("You failed.Try again")

else:
  print("You failed")